from math import sqrt
from maze_tools import load_maze, print_maze, check_bounds, paint_solution, zoom_bitmaze
from random_traversal import generate_random_traversal
from timeit import default_timer
from enum import Enum 
import copy

class Node(Enum):
	NORTH = None
	SOUTH = None
	EAST = None
	WEST = None

def depth_first_search(path):
	start_time = default_timer()
	maze, (width, heigth) = load_maze(path)
	start = maze[:width].index(1)
	finish = maze[-width:].index(1)+(width*(heigth-1))
	maze_path = [start, start+width]
	dead_ends = []
	print_path = 1
	print("This may take a while...")
	pathing = list(map(lambda x : x, maze))
	while maze_path[-1] != finish:
		a = maze_path[-1]

		pathing[a] = 2

		# TRY RIGHT
		if check_bounds(a, +1, width) and a%width < (a+1)%width and maze[a+1] and (a+1) not in maze_path and (a+1) not in dead_ends:
			maze_path.append(a+1)
			continue
		# TRY DOWN
		if check_bounds(a, +width, width) and (a+width) and maze[a+width] and (a+width) not in maze_path and (a+width) not in dead_ends:
			maze_path.append(a+width)
			continue
		# TRY LEFT
		if check_bounds(a, -1, width) and a%width > (a-1)%width and maze[a-1] and (a-1) not in maze_path and (a-1) not in dead_ends:
			maze_path.append(a-1)
			continue
		# TRY UP
		if check_bounds(a, -width, width) and (a-width) and maze[a-width] and (a-width) not in maze_path and (a-width) not in dead_ends:
			maze_path.append(a-width)
			continue
		
		dead_ends.append(maze_path.pop())
		
		pathing[a] = 1

	pathing[finish] = 2
	pathing[start] = 2
	elapsed_time = default_timer() - start_time
	#print_maze(pathing, width)
	#print(maze_path)
	print("Maze path length : {}".format(len(maze_path)))
	print("Elapsed time generating maze : {}".format(elapsed_time))
	paint_solution(pathing, width, heigth, 5, path)


if __name__ == '__main__' :
	generate_random_traversal(10, paint=True, name='search.bmp')
	find_vertices('search.bmp')
	depth_first_search('search.bmp')
