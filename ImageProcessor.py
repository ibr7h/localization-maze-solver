import cv2
import numpy as np

class ImageProcessor:
    def __init__(self,image):
        self.imageToProcess = image

    def gaussianBlur(self):
        return cv2.GaussianBlur(self.imageToProcess,(5,5),0)

    def getThresholdedImage(self,isInverted):
        threshType = cv2.THRESH_BINARY_INV if isInverted else cv2.THRESH_BINARY
        retval, threshold = cv2.threshold(self.imageToProcess,127,255,threshType)
        return threshold

    def getOtsuBinarizedImage(self,isInverted):
        image = self.blurImage()
        threshType = cv2.THRESH_BINARY_INV if isInverted else cv2.THRESH_BINARY
        retval, threshed = cv2.threshold(image,0,255,threshType + cv2.THRESH_OTSU)
        return threshed

    def getAdaptiveThreshold(self, image):
        return cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C ,\
                                    cv2.THRESH_BINARY,21,0)

    def medianBlur(self):
        return cv2.medianBlur(self.imageToProcess,9)

    def blur(self):
        return cv2.blur(self.imageToProcess,9)

    def getTopBound(self,image):
        height, width = image.shape[:2]
        for i in range(height):
            for j in range(width):
                if(image[j,i] == 255):
                    return i

    def getBottomBound(self,image):
        height, width = image.shape[:2]
        for i in reversed(range(height)):
            for j in range(width):
                if(image[j,i] == 255):
                    return i

    def getLeftBound(self,image):
        height,width = image.shape[:2]
        for i in range(width):
            for j in range(height):
                if(image[i,j] == 255):
                    return i

    def getRightBound(self,image):
        height,width = image.shape[:2]
        for i in reversed(range(width)):
            for j in range(height):
                if(image[i,j] == 255):
                    return i


    def getBounds(self,image):
        height, width = image.shape[:2]
        topBound = self.getTopBound(image)
        bottomBound = self.getBottomBound(image)
        leftBound = self.getLeftBound(image)
        rightBound = self.getRightBound(image)
        return topBound,leftBound,bottomBound,rightBound
