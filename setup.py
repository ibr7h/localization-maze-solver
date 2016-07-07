import numpy as np
import cv2
import Tkinter as Tk
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
    return cv2.imread(filename)

def setupWindow():
    image = getUserSelectedImage()
    window = cv2.namedWindow(MAZE_NAME,0)
    cv2.imshow(MAZE_NAME,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows

setupWindow()
