from PIL import Image, ImageDraw

def template_maze(side):
	maze = [None]*(side*side)
	for i in range(side):
		for j in range(side):
			if i%side == 0 or i%side == (side-1) or j%side == (side-1) or j == 0:
				maze[i + j*side] = 0
	return maze

def check_bounds(ind, offset, side):
	line = ind//side
	ans = (ind+offset > 0)
	ans = ans and (ind+offset < side*side)
	return ans

def print_maze(maze, side):
	print("|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
	for i, slot in enumerate(maze):
		print(slot, end=' ')
		if ((i+1)%(side) == 0):
			print("")
	print("|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")


def paint_maze(maze, side, name):
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

	im.save("{}.bmp".format(name), quality=100, subsampling=0)

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
			if maze[width*w + h]:
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
				draw.polygon([w*block_size,
							h*block_size,
							w*block_size + block_size,
							h*block_size,
							w*block_size + block_size,
							h*block_size + block_size,
							w*block_size,
							h*block_size + block_size],
							outline=(255,255,255))
	img.save("{}_resized.bmp".format(path[:-4]), quality=100, subsampling=0)