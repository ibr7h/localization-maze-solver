import cv2
import numpy as nps
import Queue as q
from Node import Node

class MazeSolver:

    def __init__(self,proccessedImage,granularity):
        self.image = proccessedImage
        self.height,self.width = proccessedImage.shape[:2]
        self.nodes_to_visit = q.PriorityQueue()
        self.node_distances = {}
        self.parent_nodes = {}
        self.visited_nodes = {}
        self.GRANULARITY = granularity

    def solveMaze(self,start_x,start_y,end_x,end_y):
        i = 0
        #setup
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        curr_node = Node(start_x,start_y)
        end_node = Node(end_x,end_y)
        self.node_distances[curr_node.position] = 0
        self.parent_nodes[curr_node.position] = None
        self.nodes_to_visit.put((curr_node.get_priority(end_node,0),curr_node))
        while curr_node.position!=end_node.position and not self.nodes_to_visit.empty():
            if(i%10000 == 0):
                print "Iteration {0} complete".format(i)
            _, curr_node = self.nodes_to_visit.get()
            for node in self._get_new_nodes(curr_node):
                distance = self.node_distances[curr_node.position] +self.GRANULARITY;
                if not node.position in self.node_distances or distance < self.node_distances[node.position]:
                        priority = node.get_priority(end_node,distance)
                        self.node_distances[node.position] = distance
                        self.nodes_to_visit.put((priority,node))
                        self.parent_nodes[node.position] = curr_node
            self.visited_nodes[curr_node.position] = True
            i+=1
        if curr_node.position == end_node.position:
            print("Algorithm completed. Total iterations: {0}".format(i))
            return self._get_solution_list(curr_node)
        else:
            print("No solution found")
            return False

    def _get_solution_list(self, node):
        solution = []
        current = node
        while self.parent_nodes[current.position] != None:
            solution.append(current.position)
            current = self.parent_nodes[current.position]
        solution.append((self.start_x,self.start_y))
        return solution



    def _get_new_nodes(self,parent):
        valid_new_nodes = []
        granularity = self.GRANULARITY
        if( abs(self.end_x - parent.position[0]) < granularity and
            abs(self.end_y - parent.position[1]) < granularity):
            granularity = 1

        moves = [[0,granularity],[0,-granularity],[granularity,0],[-granularity,0]]

        for move in moves:
            for i in range(granularity):
                if not self.image[parent.position[1] + (move[1]//granularity)*i,parent.position[0] + (move[0]//granularity)*i]:
                    break
            else:
                new_node = Node(*[pos+move for pos,move in zip(parent.position,move)])
                valid_new_nodes.append(new_node)
        return valid_new_nodes


    def _is_valid_node(self,position,parent):
        try:
            return not self.visited_nodes[position] == True
        except KeyError:
            pass
        return not(position in self.visited_nodes or
                   position == parent.position or
                   self.image[position[1], position[0]] == 0)
