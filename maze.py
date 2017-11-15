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
	im = Image.new('RGB', (side, side), color=(0,0,0))
	draw = ImageDraw.Draw(im)
	for ind, color in enumerate(maze):
		if color == 1:
			draw.point((ind%side, ind//side), fill=(255,255,255))
		else:
			if color == 2:
				draw.point((ind%side, ind//side), fill=(0,0,200))
			else:
				if color == 3:
					draw.point((ind%side, ind//side), fill=(200,0,0))

	im.save("{}.bmp".format(name), quality=100, subsampling=0, dpi=(100,100))



def generate_random_traversal(side):
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
			print("Generating maze... ",progress//size, "%\r", end='')

			#input(">> Next\n")
	except IndexError:
			for i, slot in enumerate(maze):
				if slot is None:
					maze[i]  = 0
	#print_maze(maze, side)
	print("")
	start = choice([i for i, v in enumerate(maze[:side]) if v == 1])
	end = choice([i+(side*(side-1)) for i, v in enumerate(maze[-side:]) if v == 1])
	maze[start] = 2
	maze[end] = 3
	paint(maze, side, side)

def load_maze(path):
	with Image.open(path) as img:
		width, height = img.size
		maze = [None]*(width*height)
		for i in range(width):
			for j in range(height):
				if img.getpixel((i, j)) == (255, 255, 255):
					maze[width*i + j] = 1
				else:
					if img.getpixel((i, j)) == (0, 0, 200):
						maze[width*i + j] = 2
					else:
						if img.getpixel((i, j)) == (200, 0, 0):
							maze[width*i + j] = 3
	return maze, (width, height)

def zoom_bitmaze(path, block_size):
	maze, (width, height) = load_maze(path)
	img = Image.new('RGB', (width*block_size, height*block_size), color=(0,0,0))
	draw = ImageDraw.Draw(img)
	for w in range(width):
		for h in range(height):
			if maze[width*w + h] == 1:
				draw.polygon([w*block_size,
							h*block_size,
							w*block_size + block_size,
							h*block_size,
							w*block_size + block_size,
							h*block_size + block_size,
							w*block_size,
							h*block_size + block_size],
							fill=(255,255,255))
			else:
				if maze[width*w + h] == 2:
						draw.polygon([w*block_size,
							h*block_size,
							w*block_size + block_size,
							h*block_size,
							w*block_size + block_size,
							h*block_size + block_size,
							w*block_size,
							h*block_size + block_size],
							fill=(0,0,200))
				else:
					if maze[width*w + h] == 3:
						draw.polygon([w*block_size,
							h*block_size,
							w*block_size + block_size,
							h*block_size,
							w*block_size + block_size,
							h*block_size + block_size,
							w*block_size,
							h*block_size + block_size],
							fill=(200,0,0))

	img.save("resized_{}".format(path), quality=100, subsampling=0)

		
		

if __name__ == "__main__" :
	generate_random_traversal(300)
	zoom_bitmaze('300.bmp', 30)




		



