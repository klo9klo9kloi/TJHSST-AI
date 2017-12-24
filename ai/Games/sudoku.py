def printMatrix(puzzle):
  
  matrix = []
  index = 0
  
  for s in puzzle:
   matrix.append(s)
   index += 1
  
  index = 0
  row = ""
  for x in range (9):
    for y in range (9):
       row += str(matrix[index])
       index+=1
    print(row)
    print("")
    row = ""
  print("")

def optimizePoss(puzzle, index):
  possible = findPossibilites(puzzle, index)
  
  if len(possible) == 1:
    return possible
  
  row = math.floor(index/9)
  col = index%9
  
  if len(rowNbrs(puzzle, index)) == 7:
    probposs1 = possible.copy()
    
    for c in range(9):
      if c != col:
        if puzzle[row * 9 + c] != index:
          if puzzle[row * 9 + c] == '.':
            probposs1 = probposs1 - findPossibilites(puzzle, row*9+c)
            if len(probposs1) == 1:
              return probposs1

  if len(colNbrs(puzzle, index)) == 7:	
    probposs2 = possible.copy()
    
    for y in range (col, col+(9*9), 9):
      if y != (row * 9 + col):
        if puzzle[y] == '.':
          probposs2 = probposs2 - findPossibilites(puzzle, y)
          if len(probposs2) == 1:
            return probposs2
  
  if len(regionNbrs(puzzle, index)) == 7:
    row2 = math.floor(row/3) * 3
    col2 = math.floor(col/3) * 3
    
    probposs3 = possible.copy()
    
    for r in range (row2, row2+3):
      for co in range (col2, col2+3):
        position = r * 9 + co
        if position != (row * 9 + col):
          if puzzle[position] != '.':
            probposs3 = probposs3 - findPossibilites(puzzle, position)
            if len(probposs3) == 1:
              return probposs3
  
  return possible
  
  
def findPossibilites(puzzle, index):
#  nbrs = findAllNbrs(puzzle, index)
#  possible = []
#  for y in range(1, 10):
#    value = str(y)
#    if value not in nbrs:
#          possible.append(y)
  rows = rowNbrs(puzzle, index)
  cols = colNbrs(puzzle, index)
  reg = regionNbrs(puzzle, index)
  
  #print(rows)
  #print(cols)
  #print(reg)
  
  numbers = set(['1','2','3','4','5','6','7','8','9'])

  
  row1 = rows ^ numbers
  col1 = cols ^ numbers
  reg1 = reg ^ numbers
  
  #print(row1)
  #print(col1)
  #print(reg1)
  
  possible = row1 & col1 & reg1
  
  
  #print(possible)
  return possible            

def findAllNbrs(puzzle, index):

  rows = rowNbrs(puzzle, index)
  cols = colNbrs(puzzle, index)
  reg = regionNbrs(puzzle, index)

  nbrs = rows + cols + reg
 
  return nbrs

def colNbrs(puzzle, index):
  row = math.floor(index/9)
  col = index%9

  nbrs = set([])
  
  for y in range (col, col+(9*9), 9):
    if y != (row * 9 + col):
      if puzzle[y] != '.':
        nbrs.add(puzzle[y])
  return nbrs

def rowNbrs(puzzle, index):
  row = math.floor(index/9)
  col = index%9

  nbrs = set([])
  
  for c in range(9):
   if c != col:
    if puzzle[row * 9 + c] != '.':
      nbrs.add(puzzle[row * 9 + c])
  return nbrs

def regionNbrs(puzzle, index):
  nbrs = set([])
  
  row = math.floor(index/9)
  col = index%9
  row2 = math.floor(row/3) * 3
  col2 = math.floor(col/3) * 3
  
  for r in range (row2, row2+3):
    for co in range (col2, col2+3):
      position = r * 9 + co
#      if position != (row * 9 + col) and (r != row) and (co != col):
      if position != (row * 9 + col):
        if puzzle[position] != '.':
          nbrs.add(puzzle[position])
  return nbrs
  
def isSolved(puzzle):
  if '.' in puzzle:
    return False
  rowset = set(['1','2','3','4','5','6','7','8','9'])
  
  for x in range(9):
    row = set([])
    for y in range(9):
      row.add(puzzle[x*9 + y])
    rowset = row&rowset
    
  if len(rowset) != 9:
    return False
  
  colset = set(['1','2','3','4','5','6','7','8','9'])
  
  for x in range(9):
    col = set([])
    for y in range(9):
      col.add(puzzle[x*9 + y])
    colset = col&colset
  if len(colset) != 9:
    return False
  
  regset = set(['1','2','3','4','5','6','7','8','9'])
  
  for x in range(0, 9, 3):
    reg = set([])
    for y in range(0, 9, 3):
      for r in range(3):
        for c in range(3):
          reg.add(puzzle[(x+r)*9 + (y+c)])
    regset = reg&regset
    
  if len(regset) != 9:
    return False
  return True
  
def solve(puzzle):
  if isSolved(puzzle):
    #printMatrix(puzzle)
    return True
  if '.' not in puzzle:
    return False
  
  #fill in forced moves
  #other constraints here
  
  index = None
  smallest = 50
  for s in range(81):
    if puzzle[s] == '.':
      temp = findPossibilites(puzzle, s)
      if len(temp) < smallest:
        smallest = len(temp)
        index = s
        
  
  poss = findPossibilites(puzzle, index)

  if len(poss) == 0:
    return False
  
  for x in poss:
    puzzle[index] = str(x)
    if solve(puzzle) == True:
      return True
    else:
      puzzle[index] = '.'
  return False    
  
  
import math
from time import time


sudoku = open('sudoku128.txt').read().split()

for x in range(128):
  test = sudoku[x]

  print("#%r" % (x+1), end="   ")
  print("")
  printMatrix(test)

  puzzle = []
  

  for s in test:
    puzzle.append(s)
  if isSolved(puzzle) == True:
    print("This is already solved.")
  else:
    tic = time()
    solve(puzzle)
    toc = time()
    print('Time = %f seconds' % ( toc - tic ) )
    printMatrix(puzzle)
    
    
    

