import numpy as np
import cv2

maze = cv2.imread("Sample Maze 1.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow('Maze Display',maze)
cv2.waitKey(0)
cv2.destroyAllWindows()
