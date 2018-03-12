import numpy as np
class PolicyGenerator(object):

	def __init__(self,image):
		self.image = image
		self.h,self.w = image.shape[:2]

	def get_critical_grid(self,border=0):
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
		self.get_reduced_graph([rows,columns])
		return [rows,columns]

	def get_reduced_graph(self,critical_grid):
		h,w = len(critical_grid[0]),len(critical_grid[1])
		expanded = []
		for i in range(2):
			print critical_grid[i][-1]
			middle_rows = [(x+y)/2 for x,y in zip(critical_grid[i][:-1],critical_grid[0][1:])]
			expanded.append([num for pair in zip(critical_grid[i],middle_rows) for num in pair] + [critical_grid[i][-1]])
		expanded_grid = [[(j,k,int(not self.image[k,j])) for j in expanded[0]] for k in expanded[1]]
		print np.array(expanded_grid)
		return expanded_grid			
