import cv2
import numpy as nps
import Queue as q

class MazeSolver:

    def __init__(self,proccessedImage):
        self.image = proccessedImage
        self.height,width = image.shape[:2]
        self.discoveredNodes = Q.PriorityQueue
        self.visitedNodes =

class Node:
    def __init__(self,x,y,prev):
        self.position = (x,y)
        self.length = prev.length +1;
        self.heuristic = MazeSolver.getHeuristic(position)
        self.previousNode = path

    def get_priority(self,end):
        return self.length + self.getStraightLine(end)

    def getStraightLine(self,end):
        return ((end.x-self.x)**2 + (end.y - self.y)**2)**0.5
