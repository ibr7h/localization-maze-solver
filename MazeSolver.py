import cv2
import numpy as nps
import Queue as q

class MazeSolver:

    def __init__(self,proccessedImage):
        self.image = proccessedImage
        self.height,self.width = proccessedImage.shape[:2]
        self.nodes_to_visit = q.PriorityQueue()
        self.discovered_nodes = []
        self.visited_nodes = []

    def solveMaze(self,start_x,start_y,end_x,end_y):
        curr_node = Node(start_x,start_y,None)
        end_node = Node(end_x,end_y,None)
        self.nodes_to_visit.put((curr_node.get_priority,curr_node))
        while curr_node.position!=end_node.position and not self.nodes_to_visit.empty():
            curr_node = self.nodes_to_visit.get()[1]
            for node in self._get_new_nodes(curr_node):
                self.discovered_nodes.append(node.position)
                priority = node.get_priority(end_node)
                self.nodes_to_visit.put((priority,node))
            self.visited_nodes.append(curr_node.position)
        if curr_node.position == end_node.position:
            print self._get_solution_list(curr_node)
            return self._get_solution_list(curr_node)
        else:
            return False

    def _get_solution_list(self, node):
        solution = []
        current = node
        while current.previousNode != None:
            solution.append(current.position)
            current = current.previousNode
        return solution



    def _get_new_nodes(self,parent):
        valid_new_nodes = []
        if self._is_valid_node((parent.position[0]+1,parent.position[1]), parent):
            valid_new_nodes.append(Node(parent.position[0]+1,
                                        parent.position[1],
                                        parent))

        if self._is_valid_node((parent.position[0]-1,parent.position[1]), parent):
            valid_new_nodes.append(Node(parent.position[0]-1,
                                        parent.position[1],
                                        parent))

        if self._is_valid_node((parent.position[0],parent.position[1]+1), parent):
            valid_new_nodes.append(Node(parent.position[0],
                                        parent.position[1]+1,
                                        parent))

        if self._is_valid_node((parent.position[0],parent.position[1]-1), parent):
            valid_new_nodes.append(Node(parent.position[0],
                                        parent.position[1]-1,
                                        parent))
        return valid_new_nodes


    def _is_valid_node(self,position,parent):
        return not(position in self.discovered_nodes or
                   position in self.visited_nodes or
                   position == parent.position or
                   self.image[position[0],position[1]] == 0)

class Node:
    HEURISTIC_DISTANCE_MULTIPLIER = 1;
    TRAVELLED_DISTANCE_MULTIPLIER = 1;

    def __init__(self,x,y,prev):
        self.position = (x,y)
        if(prev != None):
            self.length = prev.length +1
        else:
            self.length = 0
        self.previousNode = prev

    def get_priority(self,end):
        return -1*( self.TRAVELLED_DISTANCE_MULTIPLIER*self.length +
               self.HEURISTIC_DISTANCE_MULTIPLIER+self.getStraightLine(end))

    def getStraightLine(self,end):
        return ((end.position[0]-self.position[0])**2
                + (end.position[1] - self.position[1])**2)**0.5
