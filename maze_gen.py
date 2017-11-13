from sys import argv
from random import randint, choice
from PIL import Image, ImageDraw

def print_maze(maze, side):
	print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
	for i, slot in enumerate(maze):
		print(slot, end=' ')
		if ((i+1)%(side) == 0):
			print("")
	print("|||||||||||||||||||||||||||||||||||||||||||||||||||")

def check_bounds(ind, offset, side):
	line = ind//side
	ans = (ind+offset > 0)
	ans = ans and (ind+offset < side*side)
	return ans

def paint(maze, side, name):
	print("Painting...")
	im = Image.new('1', (side, side))
	draw = ImageDraw.Draw(im)
	for ind, color in enumerate(maze):
		if color:
			draw.point((ind%side, ind//side), fill=1)
	im.save("{}.bmp".format(name), quality=100, subsampling=0, dpi=(100,100))


def generate_simple():
	side = int(argv[2])
	size = side*side
	maze = [None]*size
	progress = 0;
	maze_next = set([0])
	try:
		while None in maze:

			maze_temp = set()
			a = choice(list(maze_next))
			b = 0
			try:
				if check_bounds(a, -1, side) and a%side > (a-1)%side:
					if maze[a - 1]:
						b += 1
					if maze[a - 1] is None :
						maze_temp.add(a-1)
			except:
				pass

			try:
				if check_bounds(a, +1, side) and a%side < (a+1)%side:
					if maze[a + 1]:
						b += 1
					if maze[a +  1] is None :
						maze_temp.add(a+1)
			except:
				pass

			try:
				if check_bounds(a, -side, side):
					if maze[a - side]:
						b += 1
					if maze[a - side] is None :
						maze_temp.add(a-side)
			except:
				pass
			try:
				if check_bounds(a, +side, side):
					if maze[a + side]:
						b += 1
					if maze[a + side] is None :
						maze_temp.add(a+side)
			except:
				pass

			maze[a] = 1 if b < 2 else 0

			maze_next.remove(a)

			if maze[a]:
				maze_next = maze_next | maze_temp

			progress += 100
			print("Generating maze... ",progress//size, "%\r", end='') #DEBUG

			#input(">> Next\n")
	except IndexError:
			for i, slot in enumerate(maze):
				if slot is None:
					maze[i]  = 0
	#print_maze(maze, side)
	paint(maze, side, argv[2])

		
		

if __name__ == "__main__" :
	try:
		locals()["generate_{}".format(argv[1])]()
	except (KeyError, IndexError):
		print("Usage: {} METHOD SIDE_SIZE\n Methods: \n\t simple")




		



