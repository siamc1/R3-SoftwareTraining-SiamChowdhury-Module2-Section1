#Imports pygame
import pygame
# imports shuffle and randrange functions from random to allow for easier coding
from random import shuffle, randrange
# Sets variables for the width and height of the screen in pixels, as well as the fps and half the line thickness
WIDTH = 800
HEIGHT = 800
fps = 30
widthL = 1

# Refreshes the picture of the maze
def refresh_graph(map):
	# fills the screen with white as a background
	screen.fill(white)

	# sets the coordinate pointers at the origin
	bx = 0
	by = 0

	# sets the distance between walls to a fraction of the screen dimensions
	stepX = WIDTH / len(map[0])
	stepY = HEIGHT / len(map)

	# runs through the elements in the 2D array map
	for i in range(0, len(map[0])):
		for j in range(0, len(map)):
			# creates a temporary instance of the current cell in a seperate variable
			maptemp = map[i][j]

			# checks to see which digits are ones, 1 in the thousands place refers to wall above cell and the rest going down in orders of magnitude rotate 90 degrees clockwise
			if(maptemp >= 1000):
				pygame.draw.line(screen, black, (bx, by), (bx + stepX - widthL, by))
				maptemp -= 1000
			if(maptemp >= 100):
				pygame.draw.line(screen, black, (bx + stepX - widthL, by),(bx + stepX - widthL, by + stepY - widthL)) 
				maptemp -= 100
			if(maptemp >= 10):
				pygame.draw.line(screen, black, (bx, by + stepY - widthL),(bx + stepX - widthL, by + stepY - widthL))
				maptemp -= 10
			if(maptemp >= 1):
				pygame.draw.line(screen, black, (bx, by), (bx, by + stepY - widthL))
				maptemp -= 1

			# steps the x coordinate
			bx += stepX
		# resets the x coordinate to 0 and steps the y coordinate
		bx = 0
		by += stepY

		# updates the display with the new lines
		pygame.display.update()

#Creates a graph of size n by n and returns them
def make_graph(n):
	# Creates a graph or grd with size n by  n as a 2D array
	graph = [[1111 for x in range(n)] for y in range(n)]
	# refreshes the screen
	refresh_graph(graph)
	# returns the graph as a 2D array
	return graph

# Takes in a graph and returns a randomly generated maze
def generate_maze(graph):
	# creates a boolean 2D array the size of the graph to carry values of whether the cell has been visited or not
	visited = [[False for x in range(len(graph[0]))] for y in range(len(graph))]
	# picks a random cell in the graph and sets the pointer to point to it
	x = randrange(len(visited[0]))
	y = randrange(len(visited))

	# Preforms a single step og traversing through the graph and destroys walls to form continuous paths
	def step(x, y):
		# refreshes the screen with the new map
		refresh_graph(graph)

		# sets the current cell to visited
		visited[y][x] = True
		# creates an array with all adjacent cells
		adj = [[x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]]
		#shuffles the previously created array to have a random order
		shuffle(adj)

		# runs through all of the adjacent cells to the current one and sets new pointer to their positions
		for(Cx, Cy) in adj:
			# checks to see if the given cell exists, if not it skips it, if so if it's already been visited, if so it skips it
			if Cy < 0 or Cy >= len(visited) or Cx < 0 or Cx >= len(visited[0]):
				continue
			elif visited[Cy][Cx]:
				continue

			# Checks to see which position the adjacent cell is in reference to the current cell and destroys the wall between them by subtracting the correct 1 from the cell value
			if Cx == x:
				if Cy > y:
					graph[y][x] -= 10
					graph[Cy][Cx] -= 1000
				else:
					graph[y][x] -= 1000
					graph[Cy][Cx] -= 10
			elif Cy == y:
				if Cx > x:
					graph[y][x] -= 100
					graph[Cy][Cx] -= 1
				else:
					graph[y][x] -= 1
					graph[Cy][Cx] -= 100
			# recursively calls the step function with the adjacent cell as the current cell
			step(Cx, Cy)

	#Calls the step function to start the stepping process
	step(x, y)

	# retur the graph
	return graph

# asks the user how large the maze should be and saves the answer in a variable
print("How large do you want the maze to be? ")
n = int(input())

#initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()
white = [255, 255, 255]
black = [0, 0, 0]
screen.fill(white)
pygame.display.update()

# calls the make_graph function to make a graph of size n
graph = make_graph(n)

# calls the generate_maze function to turn the graph into a maze
maze = generate_maze(graph)

# creates a boolean variable to keep track of whether the program is running or not
running = True
while running:
	#keep running at the right speed
	clock.tick(fps)
	#process input (events)
	for event in pygame.event.get():
		#check for closing the window
		if event.type == pygame.QUIT:
			running = False

