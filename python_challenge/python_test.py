#Importing Libraries
import curses
import numpy as np
import json
####################

#####################################################################
#--------------------------GAME OF LIFE-----------------------------#
#####################################################################

class GameOfLife():

  def __init__(self):

    self.get_input()
    self.init_pattern(self.load_pattern())
    self.run_game()

  def load_pattern(self):

    with open("config.json") as reader:
      json_str = reader.read()
    config = json.loads(json_str)

    return np.array(config[self.pattern.lower()], dtype=np.uint8)

  def get_input(self):

    print("Enter Pattern: ")
    self.pattern = input()

    print("Enter Number of Iterations: ")
    self.iterations = int(input())

    print("Enter Dimensions: ")
    self.rows, self.cols = tuple(map(int, input().split(',')))
    self.grid = np.zeros((self.rows, self.cols), dtype=np.uint8)

  def init_pattern(self, obj):
    r, c = obj.shape
    self.grid[5:5+r, 5:5+c] = obj

  def update(self):

      matrix = self.grid.copy()

      for i in range(self.rows):
          for j in range(self.cols):
              try:

                  neighbors = self.grid[i+1, j-1] + self.grid[i+1, j] + self.grid[i+1, j+1] + self.grid[i, j-1] + self.grid[i, j+1] + self.grid[i-1, j-1] + self.grid[i-1, j] + self.grid[i-1, j+1]

                  if (self.grid[i, j]  == 0) and (neighbors == 3): # Dead Cell
                      matrix[i, j] = 1
                  elif (self.grid[i,j] == 1) and ((neighbors == 3) or (neighbors == 2)): #Living Cell
                      matrix[i, j] = 1
                  else:
                      matrix[i, j] = 0

              except IndexError as e:
                  pass

      self.grid = matrix.copy()

  def run_game(self):
    
    screen = curses.initscr()
    win = curses.newwin(self.rows, self.cols, 0, 0)
    curses.curs_set(0)

    while self.iterations > 0:

        win.clear()
        for i in range(self.rows):
            for j in range(self.cols):
                if(self.grid[i,j] == 1):
                    win.addch(i, j, curses.ACS_DIAMOND)

        self.update()
        self.iterations -= 1
        win.refresh()

    screen.refresh()
    curses.endwin()


####################################################
#----------------Driver Code-----------------------#
gameOfLife = GameOfLife()
####################################################
