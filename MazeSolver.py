import cv2
import numpy as nps
import Queue as q

class MazeSolver:

    def __init__(self,proccessedImage):
        self.image = proccessedImage
        self.height,width = image.shape[:2]
        self.discoveredNodes = Q.PriorityQueue
