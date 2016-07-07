import numpy as np
import cv2

mazeName = 'Maze Display'
maze = cv2.imread("Sample Maze 1.png",cv2.IMREAD_GRAYSCALE)
window = cv2.namedWindow(mazeName,0)
cv2.imshow(mazeName,maze)
cv2.waitKey(0)
cv2.destroyAllWindows()
