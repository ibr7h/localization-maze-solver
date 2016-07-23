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
                if(image[j,i] == 0):
                    return i

    def getBottomBound(self,image):
        height, width = image.shape[:2]
        for i in reversed(range(height)):
            for j in range(width):
                if(image[j,i] == 0):
                    return i

    def getLeftBound(self,image):
        height,width = image.shape[:2]
        for i in range(width):
            for j in range(height):
                if(image[i,j] == 0):
                    return i

    def getRightBound(self,image):
        height,width = image.shape[:2]
        for i in reversed(range(width)):
            for j in range(height):
                if(image[i,j] == 0):
                    return i


    def getBounds(self,image):
        height, width = image.shape[:2]
        topBound = self.getTopBound(image)
        bottomBound = self.getBottomBound(image)
        leftBound = self.getLeftBound(image)
        rightBound = self.getRightBound(image)
        return topBound,leftBound,bottomBound,rightBound

    def getDefaultStart(self,image):
        height,width =image.shape[:2]
        top = self.getTopBound(image)
        for i in range(width):
            if image[top,i]!= 0:
                left = i;
                while(image[top,i]!= 0):
                    i+=1
                right = i -1;
                return int(right+left)/2,top + 3
        return (width/2, top + 3)


    def getDefaultEnd(self,image):
        height,width =image.shape[:2]
        bottom = self.getBottomBound(image)
        for i in range(width):
            if image[bottom,i]!= 0:
                left = i;
                while(image[bottom,i]!= 0):
                    i+=1
                right = i -1;
                return int(right+left)/2, bottom - 3
        return (width/2, bottom - 3)

    def mark_point(self, point, rad, colour, image):
        cv2.circle(image,point,rad,colour,-1)
        return image

    def encloseMaze(self, image):
        top,left,bottom,right = self.getBounds(image)
        cv2.rectangle(image,(left,top),(right,bottom),0,1)
        return image

    def get_granularity(self,image, num_points):
        total = 0
        height,width = image.shape[:2]

        for i in range(num_points):
            point = (randint(0,height),randint(0,width))
            while(image[point[0],point[1]] == 0):
                point = (randint(0,height),randint(0,width))
            total += self._find_closest_wall(point,height,width)point = (randint(0,height),randint(0,width))

    def _find_closest_wall(self, point,height,width):
        reachedWall = false
        distance = 0:
        while not reachedWall:
            distance +=1
            for i in range(distance):
                if(image[point[0] + i,point[1] + distance - i] == 0
                    or image[point[0] - i,point[1] + distance - i] == 0
                    or image[point[0] + i,point[1] - distance - i] == 0
                    or image[point[0] - i,point[1] - distance - i] == 0):
                    reachedWall = true
                    break;
        reurn distance
