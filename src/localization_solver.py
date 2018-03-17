from Robot import Robot

class LocalizationSolver(object):

	def __init__(self,image):
		self.image = image
		self.h,self.w = image.shape[:2]
		robot = None:
		while not robot:
			robot = Robot((self.w,self.h))
			#ensure the robot is initialized in a random location that is not a wall
			if image[robot.x,robot.y] == 0:
				robot = None


	def solve():
		#Todo: localize the robot in the maze and find a way out
		pass


	def _populate_maze():
		#Todo: populate the maze with a point cloud of robots
		pass