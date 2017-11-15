from sys import argv
from random import randint, choice
from maze_tools import template_maze, check_bounds
import os

def generate_random_traversal(_side, prints=False, paint=False, name='Default'):
	side = _side+2
	size = side*side
	maze = template_maze(side)
	progress = 0;
	#start = choice([i+side for i, v in enumerate(maze[side:side*2]) if v is None])
	start = side+1
	maze_next = set([start])
	try:
		while None in maze:

			maze_temp = set()
			a = choice(list(maze_next))
			b = 0
			# RIGHT SLOT
			if check_bounds(a, -1, side) and a%side > (a-1)%side:
				if maze[a - 1]:
					b += 1
				if maze[a - 1] is None :
					maze_temp.add(a-1)
			# LEFT SLOT
			if check_bounds(a, +1, side) and a%side < (a+1)%side:
				if maze[a + 1]:
					b += 1
				if maze[a +  1] is None :
					maze_temp.add(a+1)
			# DOWN SLOT
			if check_bounds(a, -side, side):
				if maze[a - side]:
					b += 1
				if maze[a - side] is None :
					maze_temp.add(a-side)
			# UP SLOT
			if check_bounds(a, +side, side):
				if maze[a + side]:
					b += 1
				if maze[a + side] is None :
					maze_temp.add(a+side)

			maze[a] = 1 if b < 2 else 0

			maze_next.remove(a)

			if maze[a]:
				maze_next = maze_next | maze_temp

			progress += 100
			print("Generating maze...",progress//size, "%\r", end='')

			#input(">> Next\n")
	except IndexError:
			for i, slot in enumerate(maze):
				if slot is None:
					maze[i]  = 0
	#print_maze(maze, side)
	print("Generating maze... 100%\r")
	end = [i+(side*(side-2)) for i, v in enumerate(maze[-side*2:-side]) if v == 1][-1]
	maze[start-side] = 1
	maze[end+side] = 1
	if paint:
		from tools import paint_maze
		paint_maze(maze, side, name)
	if prints:
		from tools import print_maze
		print_maze(maze, side)

	return maze
		

if __name__ == "__main__" :
	try:
		os.makedirs("Examples")
	except:
		pass
	generate_random_traversal(15, name=os.path.join('Examples','random_traversal'), paint=True)
	from maze_tools import zoom_bitmaze
	zoom_bitmaze(os.path.join('Examples','random_traversal.bmp'), 100)


