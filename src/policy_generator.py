class PolicyGenerator(object):

	def __init__(self,image):
		self.image = image
		self.h,self.w = image.shape[:2]

	def get_critical_grid(self,border=2):
		"""Assuming a square grid, this function returns the critical columns and rows of the maze"""
		columns,rows = [],[]
		last = False
		for i in range(border,self.h-border):
			consecutive = 0
			for j in range(border,self.w-border):
				#print i,j,self.image[i,j]
				if not self.image[i,j]:
					consecutive += 1
				else:
					consecutive = 0
				if consecutive  > 5:
					print last
					if not last:
						last = True
						rows.append(i)							
					break
			else:
				last = False
		last = False
		for j in range(border,self.w-border):
			consecutive = 0
			
			for i in range(border,self.h-border):
				if not self.image[i,j]:
					consecutive += 1
				else:
					consecutive = 0
				if consecutive > 5:
					if not last:
						last = True
						columns.append(j)
					break
			else:
				last = False


		print ("CRIT ROWS: " + str(rows))
		print ("CRIT COLS: " + str(columns))
		return [rows,columns]
