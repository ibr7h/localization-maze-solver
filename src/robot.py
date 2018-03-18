import numpy as np
class Robot(object):

	def __init__(self,bounds):
		self.x = random.randint(0,bounds[0]-1)
		self.y = random.randint(0,bounds[1]-1)
		self.directon = random.randint(0,3)

	def __init__(self,position):
		self.x = position[0]
		self.y = position[1]

	def measurePosition(self,map):
		h,w = map.shape[:2]
		measurement = np.zeros(4)
		directions = [[0,-1],[-1,0],[0,1],[1,0]]
		for i,direction in enmerate(directions):
			y,x = self.y,self.x
			distance = 0
			while y >= 0 and y < h and x >= 0 and x < w and map[y,x] != 0:
				y += direction[0]
				x += direction[1]
				distance += 1
			measurement[i] = distance
		return measurements


	def move(self,direction,amount=1,success_probability = 0.9):
		if random.random(0,1) < success_probability:
			self.x += direction[0]

	def probability(self,measurement):
		#TODO: write a function to guess probability that the measurements were obtained from the robot's position
