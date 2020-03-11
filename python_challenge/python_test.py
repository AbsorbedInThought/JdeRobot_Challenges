
#Importing Libraries
import curses
import numpy as np
import json
####################


def addGlider(i, j, grid):

    glider = np.array([[0,  0, 1],
                       [1,  0, 1],
                       [0,  1, 1]])
    grid[i:i+3, j:j+3] = glider

def addGosperGliderGun(i, j, grid):

    gun = np.zeros(11*38).reshape(11, 38)

    gun[5][1] = gun[5][2] = 1
    gun[6][1] = gun[6][2] = 1

    gun[3][13] = gun[3][14] = 1
    gun[4][12] = gun[4][16] = 1
    gun[5][11] = gun[5][17] = 1
    gun[6][11] = gun[6][15] = gun[6][17] = gun[6][18] = 1
    gun[7][11] = gun[7][17] = 1
    gun[8][12] = gun[8][16] = 1
    gun[9][13] = gun[9][14] = 1

    gun[1][25] = 1
    gun[2][23] = gun[2][25] = 1
    gun[3][21] = gun[3][22] = 1
    gun[4][21] = gun[4][22] = 1
    gun[5][21] = gun[5][22] = 1
    gun[6][23] = gun[6][25] = 1
    gun[7][25] = 1

    gun[3][35] = gun[3][36] = 1
    gun[4][35] = gun[4][36] = 1

    grid[i:i+11, j:j+38] = gun

def update(grid, rows, cols):

    matrix = grid.copy()

    for i in range(rows):
        for j in range(cols):

            try:

                neighbors = grid[i+1, j-1] + grid[i+1, j] + grid[i+1, j+1] + grid[i, j-1] + grid[i, j+1] + grid[i-1, j-1] + grid[i-1, j] + grid[i-1, j+1]

                if (grid[i, j]  == 0) and (neighbors == 3): # Dead Cell
                    matrix[i, j] = 1
                elif (grid[i,j] == 1) and ((neighbors == 3) or (neighbors == 2)): #Living Cell
                    matrix[i, j] = 1
                else:
                    matrix[i, j] = 0

            except IndexError as e:
                pass

    return matrix

rows, cols = 50, 50
grid = np.zeros((rows, cols), dtype=np.uint8)

CONFIG_PATH = "config.json"
with open(CONFIG_PATH) as f:
    json_str = f.read()
config = json.loads(json_str)

print("Enter Pattern: ")
pattern = input()

print("Enter Number of Iterations: ")
iterations = int(input())

obj = np.array(config[pattern.lower()], dtype=np.uint8)
r, c = obj.shape
grid[5:5+r, 5:5+c] = obj

screen = curses.initscr()
win = curses.newwin(rows, cols, 0, 0)
curses.curs_set(0)

while iterations > 0:

    win.clear()
    for i in range(rows):
        for j in range(cols):
            if(grid[i,j] == 1):
                win.addch(i, j, curses.ACS_DIAMOND)

    grid = update(grid, rows, cols)
    iterations -= 1
    win.refresh()

screen.addstr(10, 30, 'Game Ended!')
screen.refresh()
curses.endwin()
