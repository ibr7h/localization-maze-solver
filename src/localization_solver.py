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
		self.truth_measurements = self._create_measurement_matrix()


	def solve():


		#Todo: localize the robot in the maze and find a way out
		pass


	def _populate_maze(self):
		total = 0;
		probabilites = np.zeros((self.h,self.w))
		for row in range(h):
			for col in range(w):
				if self.image[row,col] != 0:
					probabilites[row,col] = 1
					total += 1.
		for row in range(h):
			for col in range(w):
				probabilites[row,col] /= total
		return probabilities

	def _create_measurement_matrix(self):
		#Generate a set of distances to each closest wall for each point in the maze
		#For use in updating probability of each location
		measurements = np.zeros((self.h,self.w,4))
		for row in range(self.h):
			last_wall = 1
			#generate left measurements
			for col in range(self.w)
				last_wall += -last_wall if self.image[row,col] == 0 else 1 
				measurements[row,col,0] = last_wall
			last_wall = 1
			#generate right measurements
			for col in range(self.w -1,-1,-1):
				last_wall += -last_wall if self.image[row,col] == 0 else 1 
				measurements[row,col,2] = last_wall
		for col in range(self.w):
			last_wall = 1
			#generate up measurements
			for row in range(self.h)
				last_wall += -last_wall if self.image[row,col] == 0 else 1 
				measurements[row,col,1] = last_wall
			last_wall = 1
			#generate down measurements
			for row in range(self.h -1,-1,-1):
				last_wall += -last_wall if self.image[row,col] == 0 else 1 
				measurements[row,col,3] = last_wall

		return measurements




