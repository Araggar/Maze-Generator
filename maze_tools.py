from PIL import Image, ImageDraw
from colour import Color

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


	im.save("{}".format(name), quality=100, subsampling=0)

def paint_solution(maze, width, heigth, block_size, path):
	size = width*heigth
	img = Image.new('RGB', (width*block_size, heigth*block_size), color=(0,0,0))
	draw = ImageDraw.Draw(img)
	n_colors = 100
	colors = []
	for color in list(Color('blue').range_to(Color("red"), n_colors)):
		colors.append([int(c*255) for c in color.rgb])
	for color in list(Color('red').range_to(Color("blue"), n_colors)):
		colors.append([int(c*255) for c in color.rgb])
	#for color in list(Color('green').range_to(Color("blue"), n_colors)):
	#	colors.append([int(c*255) for c in color.rgb])
	progress = 0
	ind = 0
	for w in range(width):
		for h in range(heigth):
			if maze[w + width*h] == 1:
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
				if maze[w + width*h] == 2:
					draw.polygon([w*block_size,
								h*block_size,
								w*block_size + block_size,
								h*block_size,
								w*block_size + block_size,
								h*block_size + block_size,
								w*block_size,
								h*block_size + block_size],
								fill=(tuple(colors[ind])))
					ind = (ind+1)%(n_colors*2)
			progress += 100
			print("Painting solution... {}%\r".format(progress//size), end='')

	print("Painting solution... 100%")
	img.save("{}_solution.bmp".format(path), quality=100, subsampling=0)

def load_maze(path):
	with Image.open(path) as img:
		width, heigth = img.size
		maze = [0]*(width*heigth)
		for i in range(width):
			for j in range(heigth):
				if img.getpixel((i, j)) == (255, 255, 255):
					maze[i + width*j] = 1
				else:
					maze[i + width*j] = 0
	return maze, (width, heigth)

def zoom_bitmaze(path, block_size):
	progress = 0
	maze, (width, heigth) = load_maze(path)
	size = width*heigth
	img = Image.new('RGB', (width*block_size, heigth*block_size), color=(0,0,0))
	draw = ImageDraw.Draw(img)
	for w in range(width):
		for h in range(heigth):
			if maze[w + width*h] == 1:
				draw.polygon([w*block_size,
							h*block_size,
							w*block_size + block_size,
							h*block_size,
							w*block_size + block_size,
							h*block_size + block_size,
							w*block_size,
							h*block_size + block_size],
							fill=(255,255,255))
			progress += 100
			print("Zooming in... {}%\r".format(progress//size), end='')

	print("Zooming in... 100%")
	img.save("{}_resized.bmp".format(path), quality=100, subsampling=0)