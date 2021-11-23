from tkinter import *
from tkinter import messagebox
import sys
import numpy as np
import copy
import random

root = Tk()
root.title("Knight's Tour Puzzle")
grid = [[62, 33, 36, 0, 60, 0, 0, 15, 0, 0],
        [0, 0, 0, 76, 37, 0, 0, 84, 0, 0],
        [32, 0, 0, 0, 78, 89, 0, 0, 82, 19],
        [0, 58, 0, 90, 93, 0, 0, 0, 13, 0],
        [64, 0, 0, 0, 86, 0, 98, 0, 0, 71],
        [0, 4, 67, 0, 0, 96, 0, 0, 41, 0],
        [0, 65, 0, 0, 0, 73, 48, 0, 0, 21],
        [0, 54, 0, 0, 0, 100, 0, 44, 0, 0],
        [0, 0, 0, 7, 24, 0, 0, 0, 0, 0],
        [53, 0, 25, 28, 51, 8, 0, 46, 0, 10]]
gridOriginal = copy.deepcopy(grid)
gridUser = copy.deepcopy(grid)

difficulty = 0

begin = Toplevel()

def gridEasy():
  global difficulty
  difficulty = 45
  begin.destroy()
  run()
def gridMedium():
  global difficulty
  difficulty = 55
  begin.destroy()
  run()
def gridHard():
  global difficulty
  difficulty=65
  begin.destroy()
  run()


def start():
  global easy, medium, hard
  
  begin.title("Choose A Difficulty")
  Label(begin, text="What difficulty would you like to select?").pack()
  easy = Button(begin, text="Easy", command=gridEasy).pack()
  medium = Button(begin, text="Medium", command=gridMedium).pack()
  hard = Button(begin, text="Hard", command=gridHard).pack()

start()


def run():
  global gridOriginal, gridUser
  stack = []

  def randomize():
    global difficulty, grid

    counter = 0
    i = random.randint(0,9)
    j = random.randint(0,9)
    

    while counter < difficulty:
      if grid[i][j] != 0 and grid[i][j] != 100:
        grid[i][j] = 0
        counter+=1
      i = random.randint(0,9)
      j = random.randint(0,9)
      

  def numIndex(num):
    global grid
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if (grid[i][j] == num):
          col = grid[i].index(num)
          row = i
          return [row, col]

  def inGrid(num):
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if (grid[i][j] == num):
          return True
    return False

  def process(grid, stack):
    num = 100
    # finding the index of num
    index = numIndex(num)
    # adding 100 to the stack to start off
    stack.append([num])

    while num > 0:
      
      # exists = False initially
      exists = False

      # check each index in stack, if one of the numbers equals num, skip the next conditional
      for i in stack:
        if i[0] == num:
          exists = True
      # if none of the numbers equal num, we can add it to the stack
      if (not exists):
        stack.append([num])

      
      # run possible() with index, num, and stack
      if (possible(gridOriginal, grid, index, num, stack)):
        
        index = numIndex(num-1)
        
        # if possible returns True (either a number was already in the grid, and it was in the range of movement from the index that we were at, or there was an empty space)
        # we will add the index where the move was made to, to the number we are currently at 
        stack[100-num].append(index)
        num-=1

        # then subtract 1 from num, and officially set the index to the new index (weird interaction with the possible method)
        
      else:
        # if it returns false, we will remove the last index of the stack, and add one to the number and find the index of num-1
        stack.pop()
        num += 1
        index = numIndex(num)
      
      if (num == 1):
        print(np.matrix(grid))
        return
      elif (num > 100):
        # if no more moves are possible, then eventually the stack will fill up and num will be greater than 100
        print("sorry, the puzzle is not possible")
        return

  def possible(gridOriginal, grid, index, num, stack):

    if (inGrid(num-1)):
      try:
        if (grid[index[0] + 2][index[1] + 1] == num-1 and [index[0]+2, index[1]+1] not in stack[100-num] and index[0] + 2 >= 0 and index[1] + 1 >= 0): # [+2, +1]

          return True
      except Exception:
        pass
      try:
        if (grid[index[0] + 2][index[1] - 1] == num-1 and [index[0]+2, index[1]-1] not in stack[100-num] and index[0] + 2 >= 0 and index[1] - 1 >= 0): # [+2, -1]
          
          return True
      except Exception:
        pass
      try:
        if (grid[index[0] + 1][index[1] + 2] == num-1 and [index[0]+1, index[1]+2] not in stack[100-num] and index[0] + 1 >= 0 and index[1] + 2 >= 0): # [+1, +2]
          
          return True
      except Exception:
        pass
      try:
        if (grid[index[0] + 1][index[1] - 2] == num-1 and [index[0]+1, index[1]-2] not in stack[100-num] and index[0] +1 >= 0 and index[1] - 2 >= 0): # [+1, -2]
          
          return True
      except Exception:
        pass
      try:
        if (grid[index[0] - 1][index[1] - 2] == num-1 and [index[0]-1, index[1]-2] not in stack[100-num] and index[0] - 1 >= 0 and index[1] - 2 >= 0): # [-1, -2]
          
          return True
      except Exception:
        pass
      try:
        if (grid[index[0] - 1][index[1] + 2] == num-1 and [index[0]-1, index[1]+2] not in stack[100-num] and index[0] - 1 >= 0 and index[1] + 2 >= 0): # [-1, +2]
          
          return True
      except Exception:
        pass
      try: 
        if (grid[index[0] - 2][index[1] - 1] == num-1 and [index[0]-2, index[1]-1] not in stack[100-num] and index[0] - 2 >= 0 and index[1] - 1 >= 0): # [-2, -1]
          
          return True
      except Exception:
        pass
      try: 
        if (grid[index[0] - 2][index[1] + 1] == num-1 and [index[0]-2, index[1]+1] not in stack[100-num] and index[0] - 2 >= 0 and index[1] + 1 >= 0): # [-2, +1]
          return True
      except Exception:
        pass
      if grid[index[0]][index[1]] != gridOriginal[index[0]][index[1]]:
        grid[index[0]][index[1]] = 0
      return False
    else:
      try:
        if (grid[index[0] + 2][index[1] + 1] == 0 and [index[0]+2, index[1]+1] not in stack[100-num] and index[0] + 2 >= 0 and index[1] + 1 >= 0): # [+2, +1]
          
          grid[index[0]+2][index[1]+1] = num-1
          return True
      except Exception:
        pass
      try: 
        if (grid[index[0] + 2][index[1] - 1] == 0 and [index[0]+2, index[1]-1] not in stack[100-num] and index[0] + 2 >= 0 and index[1] - 1 >= 0): # [+2, -1]
          
          grid[index[0]+2][index[1]-1] = num-1
          return True
      except Exception:
        pass
      try: 
        if (grid[index[0] + 1][index[1] + 2] == 0 and [index[0]+1, index[1]+2] not in stack[100-num] and index[0] + 1 >= 0 and index[1] + 2 >= 0): # [+1, +2]
          
          grid[index[0]+1][index[1]+2] = num-1
          return True
      except Exception:
        pass
      try: 
        if (grid[index[0] + 1][index[1] - 2] == 0 and [index[0]+1, index[1]-2] not in stack[100-num] and index[0] + 1 >= 0 and index[1] - 2 >= 0): # [+1, -2]
          
          grid[index[0] + 1][index[1] - 2] = num-1
          return True
      except Exception:
        pass
      try: 
        if (grid[index[0] - 1][index[1] - 2] == 0 and [index[0]-1, index[1]-2] not in stack[100-num] and index[0] - 1 >= 0 and index[1] - 2 >= 0): # [-1, -2]
          
          grid[index[0]-1][index[1]-2] = num-1
          return True
          
      except Exception:
        pass
      try: 
        if (grid[index[0] - 1][index[1] + 2] == 0 and [index[0]-1, index[1]+2] not in stack[100-num] and index[0] - 1 >= 0 and index[1] + 2 >= 0): # [-1, +2]
    
          grid[index[0]-1][index[1]+2] = num-1
          return True
      except Exception:
        pass
      try: 
        if (grid[index[0] - 2][index[1] - 1] == 0 and [index[0]-2, index[1]-1] not in stack[100-num] and index[0] - 2 >= 0 and index[1] - 1 >= 0): # [-2, -1]
          
          grid[index[0]-2][index[1]-1] = num-1
          return True
      except Exception:
        pass
      try: 
        if (grid[index[0] - 2][index[1] + 1] == 0 and [index[0]-2, index[1]+1] not in stack[100-num] and index[0] - 2 >= 0 and index[1] + 1 >= 0): # [-2, +1]
          grid[index[0]-2][index[1]+1] = num-1
          return True
      except Exception:
        pass
      if grid[index[0]][index[1]] != gridOriginal[index[0]][index[1]]:
        grid[index[0]][index[1]] = 0
      return False

  process(grid, stack)

  randomize()

  gridOriginal = copy.deepcopy(grid)
  gridUser = copy.deepcopy(grid)

  def userPossible(gridUser, index, num):
    if (inGrid(num-1)):
      try:
        if (gridUser[index[0] + 2][index[1] + 1] == num-1 and index[0] + 2 >= 0 and index[1] + 1 >= 0): # [+2, +1]

          return True
      except Exception:
        pass
      try:
        if (gridUser[index[0] + 2][index[1] - 1] == num-1 and index[0] + 2 >= 0 and index[1] - 1 >= 0): # [+2, -1]
          
          return True
      except Exception:
        pass
      try:
        if (gridUser[index[0] + 1][index[1] + 2] == num-1 and index[0] + 1 >= 0 and index[1] + 2 >= 0): # [+1, +2]
          
          return True
      except Exception:
        pass
      try:
        if (gridUser[index[0] + 1][index[1] - 2] == num-1 and index[0] +1 >= 0 and index[1] - 2 >= 0): # [+1, -2]
          
          return True
      except Exception:
        pass
      try:
        if (gridUser[index[0] - 1][index[1] - 2] == num-1 and index[0] - 1 >= 0 and index[1] - 2 >= 0): # [-1, -2]
          
          return True
      except Exception:
        pass
      try:
        if (gridUser[index[0] - 1][index[1] + 2] == num-1 and index[0] - 1 >= 0 and index[1] + 2 >= 0): # [-1, +2]
          
          return True
      except Exception:
        pass
      try: 
        if (gridUser[index[0] - 2][index[1] - 1] == num-1 and index[0] - 2 >= 0 and index[1] - 1 >= 0): # [-2, -1]
          
          return True
      except Exception:
        pass
      try: 
        if (gridUser[index[0] - 2][index[1] + 1] == num-1 and index[0] - 2 >= 0 and index[1] + 1 >= 0): # [-2, +1]
          return True
      except Exception:
        pass
    return False

  new_items = []
  field_indices = []
  counter = -1

  def numIndexUser(num):
    global gridUser
    for i in range(len(gridUser)):
      for j in range(len(gridUser[i])):
        if (gridUser[i][j] == num):
          col = gridUser[i].index(num)
          row = i
          return [row, col]

  def checkGrid(field_indices):
    num = 100
    index = numIndexUser(num)
    while True:
      if (userPossible(gridUser, index, num)):
        if (index in field_indices):
          new_items[field_indices.index(index)]["bg"] = "green"
        num-=1
        index = numIndexUser(num)
      else:
        if (index in field_indices):
          new_items[field_indices.index(index)]["bg"] = "red"
        return False
      if (num == 1):
        return True

  # if the number that the user entered was incorrect, highlight the square where it was incorrect
  # if they were correct, highlight the square green

  def userSolution():
    global gridUser
    incomplete = False
    for i in new_items:
      i["bg"] = "white"

    for index in range(len(field_indices)):
      isint = True
      try:
        int(new_items[index].get("1.0", "end-1c"))
      except Exception:
        isint = False
        pass

      if (new_items[index].get("1.0", "end-1c") != '' and isint):
        gridUser[field_indices[index][0]][field_indices[index][1]] = int(new_items[index].get("1.0", "end-1c"))
      else:
        gridUser[field_indices[index][0]][field_indices[index][1]] = 0
        new_items[index]["bg"] = "blue"
        incomplete = True
      
    if not incomplete:
      if (checkGrid(field_indices) == True):
        messagebox.showinfo("Good Job!", "Nice work, your solution to the puzzle is correct!")
        sys.exit()
      else:
        messagebox.showinfo("Nice Try!", "Sorry, your grid does not match")
    else:
      messagebox.showerror("Error: Incomplete Information", "The boxe(s) highlighted in blue have incomplete/invalid information (please enter a number)")

  def solve():
    global grid
    stack = []
    process(grid, stack)

  def clearText():
    for i in range(len(new_items)):
      new_items[i].delete("1.0", "end-1c")
      new_items[i]["bg"] = "white"

  for i in range(10):
      for j in range(10):
          if grid[i][j] != 0:
            lbl = Label(root, text=str(grid[i][j]), font=("Courier", 20), padx=20, pady=20)
            lbl.grid(row=i, column=j)
          else:
            e = Text(root, width=5, height=2)
            e.grid(row=i, column=j)
            counter+=1
            new_items.append(e)
            field_indices.append([i, j])

  btn = Button(root, text = "Check Answers", command=userSolution)
  btn.grid(row=11, column=0)

  clearBtn = Button(root, text="Clear", command=clearText)
  clearBtn.grid(row = 11, column=9)

  solveBtn = Button(root, text = "Solve", command=solve)
  solveBtn.grid(row=12, column=0)
  

root.resizable(width=False, height=False)
root.mainloop()