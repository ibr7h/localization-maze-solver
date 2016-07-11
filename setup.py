import numpy as np
import cv2
import Tkinter as Tk
import sys
from ImageProcessor import ImageProcessor
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
    image = getUserSelectedImage()
    imageProcessor = ImageProcessor(image)
    image = imageProcessor.getThresholdedImage(True)
    window = cv2.namedWindow(MAZE_NAME,0)
    cv2.createTrackbar("trackbar",MAZE_NAME,0,255,testFuc)
    cv2.imshow(MAZE_NAME,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows

setupWindow()
