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
    return cv2.imread(filename, 0)

def testFuc(x):
    pass

def setupWindow():
    original_image = getUserSelectedImage()
    imageProcessor = ImageProcessor(original_image)
    image = imageProcessor.getThresholdedImage(False)
    window = cv2.namedWindow(MAZE_NAME,0)
    cv2.createTrackbar("trackbar",MAZE_NAME,0,255,testFuc)
    image = imageProcessor.encloseMaze(image)
    mazerunner = MazeSolver.MazeSolver(image);
    start_x,start_y = imageProcessor.getDefaultStart(image)
    end_x, end_y = imageProcessor.getDefaultEnd(image)

    solution = mazerunner.solveMaze(start_x,start_y,end_x,end_y)
    if(not solution):
        cv2.imshow(MAZE_NAME,image)
    else:
        solvedImage = draw_solution(solution,original_image)
        solvedImage[start_y,start_x] = 30
        solvedImage[start_y,start_x] = 30
        cv2.imshow(MAZE_NAME,solvedImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows

def draw_solution(path,image):
    for coordinate in path:
        image[coordinate[1],coordinate[0]] = 120;
    return image

setupWindow()
