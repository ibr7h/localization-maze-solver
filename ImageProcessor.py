import cv2
import numpy as np

class ImageProcessor:
    def __init__(self,image):
        self.imageToProcess = image

    def blurImage(amount):
        return cv2.GaussianBlur(imageToProcess,(5,5),0)

    def getThresholdedImage(self,isInverted):
        threshType = cv2.THRESH_BINARY_INV if isInverted else cv2.THRESH_BINARY
        retval, threshold = cv2.threshold(self.imageToProcess,127,255,threshType)
        return threshold
