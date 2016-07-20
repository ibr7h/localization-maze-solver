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

    get_start_points(image)
    image = imageProcessor.encloseMaze(image)
    mazerunner = MazeSolver.MazeSolver(image)

    solution = mazerunner.solveMaze(start_x,start_y,end_x,end_y)
    if(not solution):
        cv2.imshow(MAZE_NAME,image)
    else:
        solvedImage = draw_solution(solution,cv2.imread(filename,1))
        solvedImage = imageProcessor.mark_point((end_x,end_y),3,(255,0,0),solvedImage)
        solvedImage = imageProcessor.mart_point((start_x,start_y),3,(255,0,0),solvedImage)
        cv2.imshow(MAZE_NAME,solvedImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows

def draw_solution(path,image):
    for coordinate in path:
        image[coordinate[1],coordinate[0]] = [0,255,0];
    return

def get_start_points(image):
    window = cv2.imshow(MAZE_NAME,image)
    print("Please \'A\' to use default start and end points, or press \'S\' to choose your own)")

    while(True):
        key = cv2.waitKey(0)
        if key == ord('a'):
            print("Using Default Start and End Points")
            start_x,start_y = imageProcessor.getDefaultStart(image)
            end_x, end_y = imageProcessor.getDefaultEnd(image)
            return start_x,start_y,end_x,end_y
        elif key == ord ('s'):
            print("Please select a start point")
            start_x,end_x = get_user_selected_point(image):
            print ("Start Point: {0}, please select an end point".format((start_x,start_y)))
            end_x,end_y = get_user_selected_point(image)
            print("End Pont: {0}".format((end_x,end_y)))
            break
        else:
            print("Invalid")
            continues

def get_user_selected_point(image):
    x, y = cv2.setMouseCallBack(MAZE_NAME,get_mouse_point)
    return x,y

def get_mouse_point(event,x,y,flags,param):
    return x,y

setupWindow()
