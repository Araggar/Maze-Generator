from math import sqrt
from maze_tools import load_maze, print_maze, check_bounds, paint_solution, zoom_bitmaze
from random_traversal import generate_random_traversal

def depth_first_search(path):
	maze, (width, heigth) = load_maze(path)
	start = maze[:width].index(1)
	finish = maze[-width:].index(1)+(width*(heigth-1))
	maze_path = [start, start+width]
	dead_ends = []
	print_path = 1
	pathing = [None]*(width*heigth)
	print("This may take a while...")
	for i, s in enumerate(maze):
		pathing[i] = 1 if s else 0
	while maze_path[-1] != finish:
		a = maze_path[-1]

		pathing[a] = 2

		# TRY 
		if check_bounds(a, -1, width) and a%width > (a-1)%width and maze[a-1] and (a-1) not in maze_path and (a-1) not in dead_ends:
			maze_path.append(a-1)
			continue
		# LEFT SLOT
		if check_bounds(a, +1, width) and a%width < (a+1)%width and maze[a+1] and (a+1) not in maze_path and (a+1) not in dead_ends:
			maze_path.append(a+1)
			continue
		# DOWN SLOT
		if check_bounds(a, -width, width) and (a-width) and maze[a-width] and (a-width) not in maze_path and (a-width) not in dead_ends:
			maze_path.append(a-width)
			continue
		# UP SLOT
		if check_bounds(a, +width, width) and (a+width) and maze[a+width] and (a+width) not in maze_path and (a+width) not in dead_ends:
			maze_path.append(a+width)
			continue
		dead_ends.append(maze_path.pop())
		pathing[a] = 1

	pathing[finish] = 2
	pathing[start] = 2
	#print_maze(pathing, width)
	#print(maze_path)
	print("Maze path length : {}".format(len(maze_path)))
	paint_solution(pathing, width, heigth, 30, path)





if __name__ == '__main__' :
	generate_random_traversal(100, paint=True, name='search.bmp')
	depth_first_search('search.bmp')
