# RyersonR3-SoftwareTraining-SiamChowdhury-Module2-Section1
 Second training module for the controls team in Ryerson Rams Robotics
 I implemented Randomized depth-first search to randomly generate mazes of size n by n given n.
 It works by first creating a grid of n by n cells, with each cell having four walls, signified by a cell value of 1111, which is stored in an integer 2D array.
 The cell value corresponds to a set of ones and zeros referring to whether the wall in theat position exists or not.
 The thousands place refers to the top wall, the hundreds the right, the tens the bottom and the ones the left.
 It then picks a random cell to start off with. THe pointer is set to that cell and the stepping process begins.
 first, it randomly selects an unvisited neighbouring cell, and breaks the wall between them by subtracting the correct 1 from the cell values of both.
 It then moves the pointer to the randomly selected neighbouring cell and recursively calls the step function again to step the new cell.
 This algorythm usually forms many simple hallways, without many forks, It does create a perfect maze, with no unvisitable places from any starting position.
 
