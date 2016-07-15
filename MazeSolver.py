import cv2
import numpy as nps
import Queue as q

class MazeSolver:

    def __init__(self,proccessedImage):
        self.image = proccessedImage
        self.height,width = image.shape[:2]
        self.discovered_nodes = []
        self.nodes_to_visit = Q.PriorityQueue()
        self.visited_nodes = []

    def solveMaze(self,start,end):
        curr_node = Node(start.x,start.y,None)
        end_node = Node(end.x,end.y,None)
        self.nodes_to_visit.put((curr_node.get_priority,curr_nodes))
        while curr_node.position!=end_node.position && not Queue.empty():
            curr_node = nodes_to_visit.get()
            for node in self._get_new_nodes(curr_node):
                priority = node.get_priority(end_node)
                discovered_nodes.append(node.position)
                nodes_to_visit.put((priority,node))
            



    def _get_new_nodes(self,parent):
        valid_new_nodes = []
        if self._is_valid_node((parent.position.x+1,parent.position.y), parent):
            valid_new_nodes.append(Node(parent.position.x+1,
                                        parent.position.y,
                                        parent))

        if self._is_valid_node((parent.position.x-1,parent.position.y), parent):
            valid_new_nodes.append(Node(parent.position.x-1,
                                        parent.position.y,
                                        parent))

        if self._is_valid_node((parent.position.x,parent.position.y+1), parent):
            valid_new_nodes.append(Node(parent.position.x,
                                        parent.position.y+1,
                                        parent))

        if self._is_valid_node((parent.position.x,parent.position.y-1), parent):
            valid_new_nodes.append(Node(parent.position.x,
                                        parent.position.y-1,
                                        parent))
        return valid_new_nodes


    def _is_valid_node(self,posiiton,parent):
        return not(position in self.discovered_nodes or
                   position in self.visited_nodes
                   position == parent.position or

                   self.image[position.x,position.y] = 0)

class Node:
    HEURISTIC_DISTANCE_MULTIPLIER = 1;
    TRAVELLED_DISTANCE_MULTIPLIER = 1;

    def __init__(self,x,y,prev):
        self.position = (x,y)
        self.length = prev.length +1;
        self.heuristic = MazeSolver.getHeuristic(position)
        self.previousNode = path

    def get_priority(self,end):
        return -1*( TRAVELLED_DISTANCE_MULTIPLIER*self.length +
               HEURISTIC_MULTIPLIER+self.getStraightLine(end))

    def getStraightLine(self,end):
        return ((end.x-self.x)**2 + (end.y - self.y)**2)**0.5
