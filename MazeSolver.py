import cv2
import numpy as nps
import Queue as q

class MazeSolver:

    def __init__(self,proccessedImage):
        self.image = proccessedImage
        self.height,width = image.shape[:2]
        self.discovered_nodes = Q.PriorityQueue()
        self.visited_nodes = []

    def solveMaze(self,start,end):
        curr_node = Node(start.x,start.y,None)
        end_node = Node(end.x,end.y,None)
        
        while curr_node.position!=end_node.position && not Queue.empty():
            for nodes in self._get_new_nodes(curr_node):
                #Get priority
                #add to discovered_nodes
                #dequeue next-best node

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


    def _is_valid_node(posiiton,parent):

class Node:
    HEURISTIC_DISTANCE_MULTIPLIER = 1;
    TRAVELLED_DISTANCE_MULTIPLIER = 1;

    def __init__(self,x,y,prev):
        self.position = (x,y)
        self.length = prev.length +1;
        self.heuristic = MazeSolver.getHeuristic(position)
        self.previousNode = path

    def get_priority(self,end):
        return TRAVELLED_DISTANCE_MULTIPLIER*self.length +
               HEURISTIC_MULTIPLIER+self.getStraightLine(end)

    def getStraightLine(self,end):
        return ((end.x-self.x)**2 + (end.y - self.y)**2)**0.5
