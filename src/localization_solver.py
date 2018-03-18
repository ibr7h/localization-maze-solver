from Robot import 
import numpy as np

class LocalizationSolver(object):

	def __init__(self,image):
		self.image = image
		self.h,self.w = image.shape[:2]
		robot = None:
		while not robot:
			robot = Robot((self.w,self.h))
			#ensure the robot is initialized in a random location that is not a wall
			if image[robot.x,robot.y] == 0:
				print "Robot initialized in a wall, retrying"
				robot = None
		self.probabilites = self._populate_maze()


	def solve():


		#Todo: localize the robot in the maze and find a way out
		pass


	def _populate_maze(self):
		total = 0;
		probabilites = np.zeros((self.h,self.w))
		for row in range(h):
			for col in range(w):
				if self.image[column,row] != 0:
					probabilites[column,row] = 1
					total += 1.
		for row in range(h):
			for col in range(w):
				probabilites[column,row] /= total
		return probabilities

