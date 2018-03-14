import numpy as np
from Queue import PriorityQueue
import sys
class PolicyGenerator(object):

	def __init__(self,image):
		self.image = image
		self.h,self.w = image.shape[:2]
		self.default_graph = [[image[i,j] == 0 for i in range(self.h)] for j in range(self.w)]

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


		self.get_reduced_graph([rows,columns])
		return [rows,columns]

	def get_reduced_graph(self,critical_grid):
		h,w = len(critical_grid),len(critical_grid[0])
		expanded = []
		for i in range(2):
			middle_rows = [(x+y)/2 for x,y in zip(critical_grid[i][:-1],critical_grid[0][1:])]
			expanded.append([num for pair in zip(critical_grid[i],middle_rows) for num in pair] + [critical_grid[i][-1]])
		expanded_grid = [[int(not self.image[k,j]) for j in expanded[0]] for k in expanded[1]]
		mapping_grid = [[(j,k) for j in expanded[0]] for k in expanded[1]]
		return expanded_grid,mapping_grid			

	def generate_policy(self,end,reduced_map=None):
		if not reduced_map:
			reduced_map = self.default_graph
		h,w = len(reduced_map),len(reduced_map[0])
		DIRS = [-1,0],[0,1],[1,0],[0,-1]
		distances = [[sys.maxint] * w for _ in range(h)]
		directions = [[-1] * w for _ in range(h)]
		distances = PriorityQueue()
		distances.put((0,end))
		visited = set()
		todo = {}
		while(not distances.empty()):
			if not distances.qsize() % (h*w/5):
				print "{0} nodes visited".format(len(visited))
			min_dist,min_node = distances.get()
			if min_node not in visited:
				for i,direction in enumerate(DIRS):
					candidate = (min_node[0] + direction[0],min_node[1] + direction[1])
					if candidate[0] >= 0 and candidate[0] < h and candidate[1] >=0 and candidate[1] < w and candidate not in visited and not reduced_map[candidate[0]][candidate[1]]:
						if candidate not in todo or min_dist + 1 < todo[candidate]: 
							distances.put((min_dist + 1,candidate))	
							todo[candidate] = min_dist + 1
							directions[candidate[0]][candidate[1]] = DIRS[(i+2)%4]
				visited.add(min_node)
		return directions










