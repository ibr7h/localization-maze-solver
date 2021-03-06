import numpy as np
import cv2
import Tkinter as Tk
import sys
from image_processor import ImageProcessor
from policy_generator import PolicyGenerator
from maze_solver import MazeSolver
from tkFileDialog import askopenfilename

MAZE_NAME = "Maze Display Window"
point = (-1,-1)

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

def setupWindow():
    filename = getUserSelectedImage()
    imageProcessor = ImageProcessor(cv2.imread(filename,0))
    colourImage = cv2.imread(filename,1)
    image = imageProcessor.getThresholdedImage(False)
    granularity = imageProcessor.get_granularity(image, 100)
    print("Granularity: {0}".format(granularity))
    start_x,start_y,end_x,end_y = get_start_points(image)
    image = imageProcessor.encloseMaze(image)
    pg = PolicyGenerator(image)
    rows,cols = pg.get_critical_grid()
    graph,mapping = pg.get_reduced_graph([rows,cols])
    policy = pg.generate_policy((end_x,end_y))
    solution = solve_using_policy(policy,(start_x,start_y),(end_x,end_y))
    imageProcessor.draw_policy(colourImage,policy)
    imageProcessor.mark_point((end_x,end_y),3,(255,0,0),colourImage)
    #cv2.imshow(MAZE_NAME,policy_image)
    mazerunner = MazeSolver(image,granularity)
    #solution = mazerunner.solveMaze(start_x,start_y,end_x,end_y)
    if(not solution):
        cv2.imshow(MAZE_NAME,image)
    else:
        solvedImage = draw_solution(solution, colourImage)
        solvedImage = imageProcessor.mark_point((start_x,start_y),3,(255,0,0),solvedImage)
        window = cv2.namedWindow("Solved Image", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Solved Image", 900,900)
        cv2.moveWindow("Solved Image",100,100)
        cv2.imshow("Solved Image",solvedImage)
    print("Press any key to exit")
    cv2.waitKey(0)
    cv2.destroyAllWindows

def solve_using_policy(policy,start,end):
    path = []
    curr = start
    while curr != end:
        path.append(curr)
        move = policy[curr[0]][curr[1]]
        curr = (curr[0] + move[0], curr[1]+move[1])
    path.append(curr)
    return path

def draw_solution(path,image):
    for i in range(len(path) -1):
        current_point = path[i]
        next_point = path[i+1]
        cv2.line(image,current_point,next_point,(0,0,200),2)
    return image

def get_start_points(image):
    window = cv2.namedWindow(MAZE_NAME, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(MAZE_NAME, 900,900)
    cv2.imshow(MAZE_NAME,image)
    cv2.moveWindow(MAZE_NAME,100,100)
    imageProcessor = ImageProcessor(image)
    start_x,start_y = imageProcessor.getDefaultStart(image)
    end_x, end_y = imageProcessor.getDefaultEnd(image)
    print("Please \'A\' to use default start and end points, or press \'S\' to choose your own)")
    key = cv2.waitKey(2000)
    print key
    if key == ord('a') or key == -1:
        print("Using Default Start and End Points")
        imageProcessor = ImageProcessor(image)
        start_x,start_y = imageProcessor.getDefaultStart(image)
        end_x, end_y = imageProcessor.getDefaultEnd(image)
        print("Start Point: {0}, End Point: {1}".format((start_x,start_y),(end_x,end_y)))
    elif key == ord ('s'):
        print("Please select a start point")
        start_x,start_y = get_user_selected_point(image)
        print ("Start Point: {0}, please select an end point".format((start_x,start_y)))
        end_x,end_y = get_user_selected_point(image)
        print("End Pont: {0}".format((end_x,end_y)))
    cv2.destroyAllWindows()
    return start_x,start_y,end_x,end_y

def get_user_selected_point(image):
    global point
    point = (-1,-1)
    cv2.setMouseCallback(MAZE_NAME,get_mouse_point)
    print("Press any key once you have selected your point")
    while point == (-1,-1):
        cv2.waitKey(0)
        if(point == (-1,-1)):
            print("Invalid pont, please try again")
    return point[0],point[1]

def get_mouse_point(event,x,y,flags,param):
    global point
    if event == cv2.EVENT_LBUTTONUP:
        print("Point {0},{1} selected".format(x,y))
        point = (x,y)

setupWindow()
