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
  
  
def findPossibilites(puzzle, index):
  nbrs = findAllNbrs(puzzle, index)
  possible = []
  for y in range(1, 10):
    value = str(y)
    if value not in nbrs:
          possible.append(y)
  return possible            

def findAllNbrs(puzzle, index):

  row = math.floor(index/9)
  col = index%9
  
  rows = rowNbrs(puzzle, index)
  cols = colNbrs(puzzle, index)
  reg = regionNbrs(puzzle, index)

  nbrs = rows + cols + reg
 
  return nbrs

def colNbrs(puzzle, index):
  row = math.floor(index/9)
  col = index%9

  nbrs = []
  
  for y in range (col, col+(9*9), 9):
    if y != (row * 9 + col):
      if puzzle[y] != '.':
        nbrs.append(puzzle[y])
  return nbrs

def rowNbrs(puzzle, index):
  row = math.floor(index/9)
  col = index%9

  nbrs = []
  for c in range(9):
   if c != col:
    if puzzle[row * 9 + c] != '.':
      nbrs.append(puzzle[row * 9 + c])
  return nbrs

def regionNbrs(puzzle, index):
  nbrs = []
  
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
          nbrs.append(puzzle[position])
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
    printMatrix(puzzle)
    return True
  if '.' not in puzzle:
    return False
  
  index = 0
  for s in puzzle:
    if s == '.':
      index = puzzle.index(s)
      break
  
  poss = findPossibilites(puzzle, index)
  
  for x in poss:
    puzzle[index] = str(x)
    if solve(puzzle) == True:
      return True
    else:
      puzzle[index] = '.'
  return False    
  
  
import math


sudoku = open('sudoku128.txt').read().split()

for x in range(51, 52):
  test = sudoku[x]

  printMatrix(test)

  puzzle = []

  for s in test:
    puzzle.append(s)
  
  if isSolved(puzzle) == True:
    print("This is already solved.")
  else:
    print(x)
    solve(puzzle)

