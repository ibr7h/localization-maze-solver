
class Robot(object):

	def __init__(self,bounds):
		self.x = random.randint(0,bounds[0]-1)
		self.y = random.randint(0,bounds[1]-1)
		self.directon = random.randint(0,3)

	def __init__(self,position,direction):
		self.x = position[0]
		self.y = position[1]
		self.direction = direction

	def measurePosition(self,map):
		#TODO: add a function to measure position to nearest wall in each direction
		pass

	def move(self,amount=1):
		#TODO: add a function to update the robot position
		pass

	def probability(self,measurement):
		#TODO: write a function to guess probability that the measurements were obtained from the robot's position
