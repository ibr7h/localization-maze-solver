import numpy as np
import cv2
import Tkinter as Tk
import sys
from ImageProcessor import ImageProcessor
import MazeSolver
from tkFileDialog import askopenfilename

MAZE_NAME = "Maze Display Window"

def getUserSelectedFilePath():
    root = Tk.Tk()
    root.withdraw()
    filepath = askopenfilename()
    return filepath

def getUserSelectedImage():
    filename = " "
    while not ".png" in filename :
        print("Please Select a .png maze image")
        filename = getUserSelectedFilePath()
    return filename

def testFuc(x):
    pass

def setupWindow():
    filename = getUserSelectedImage()
    imageProcessor = ImageProcessor(cv2.imread(filename,0))
    image = imageProcessor.getThresholdedImage(False)
    window = cv2.namedWindow(MAZE_NAME,0)
    cv2.createTrackbar("trackbar",MAZE_NAME,0,255,testFuc)
    start_x,start_y = imageProcessor.getDefaultStart(image)
    end_x, end_y = imageProcessor.getDefaultEnd(image)
    image = imageProcessor.encloseMaze(image)
    mazerunner = MazeSolver.MazeSolver(image)

    solution = mazerunner.solveMaze(start_x,start_y,end_x,end_y)
    if(not solution):
        cv2.imshow(MAZE_NAME,image)
    else:
        solvedImage = draw_solution(solution,cv2.imread(filename,1))
        solvedImage[start_y,start_x] = [1,0,0]
        solvedImage[start_y,start_x] = [1,0,0]
        cv2.imshow(MAZE_NAME,solvedImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows

def draw_solution(path,image):
    for coordinate in path:
        image[coordinate[1],coordinate[0]] = [0,255,0];
    return image

setupWindow()
