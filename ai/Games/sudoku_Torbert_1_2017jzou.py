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

  rows = rowNbrs(puzzle, index)
  cols = colNbrs(puzzle, index)
  reg = regionNbrs(puzzle, index)
  

  numbers = set(['1','2','3','4','5','6','7','8','9'])

  
  row1 = rows ^ numbers
  col1 = cols ^ numbers
  reg1 = reg ^ numbers

  
  possible = row1 & col1 & reg1
  
  return possible            

def findAllNbrs(index):
  nbrs = []
  
  row = math.floor(index/9)
  col = index%9
  
  row2 = math.floor(row/3) * 3
  col2 = math.floor(col/3) * 3
  
  #row
  for c in range(9):
      if c != col:
           nbrs.append(row * 9 + c)  
  #column
  for y in range (col, col+(9*9), 9):
      if y != (row * 9 + col):
           nbrs.append(y)
           
  #region
  for r in range (row2, row2+3):
      for co in range (col2, col2+3):
        position = r * 9 + co
        if position != (row * 9 + col):
             nbrs.append(position)
             
             
  return nbrs

def findRowNbrs(index):
  nbrs = []
  
  row = math.floor(index/9)
  col = index%9
  for c in range(9):
    if c != col:
        nbrs.append(row * 9 + c)
  return nbrs

def findColNbrs(index):
  nbrs = []
  
  row = math.floor(index/9)
  col = index%9
  for y in range (col, col+(9*9), 9):
      if y != (row * 9 + col):
           nbrs.append(y)
  return nbrs

def findRegNbrs(index):
  nbrs = []
  
  row = math.floor(index/9)
  col = index%9
  
  row2 = math.floor(row/3) * 3
  col2 = math.floor(col/3) * 3
  for r in range (row2, row2+3):
      for co in range (col2, col2+3):
        position = r * 9 + co
        if position != (row * 9 + col):
             nbrs.append(position)
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

def deduction(puzzle, index, dictionary, possible, rown, coln, regn):
  if len(possible) > 1:   
    uniqueposs = possible.copy()

    rowneigh = rown[index]
    colneigh = coln[index]
    regneigh = regn[index]
    
    #row
    rowset = set([])
    for row in rowneigh:
        if puzzle[row] == '.':
             rowset = rowset | dictionary[row]
             
    uniqueposs = uniqueposs - rowset
    
    if len(uniqueposs) == 1:
      return uniqueposs
    
    uniqueposs = possible.copy()
    
    #column
    colset = set([])
    for y in colneigh:
          if puzzle[y] == '.':
             colset = colset | dictionary[y]
    
    uniqueposs = uniqueposs - colset
    if len(uniqueposs) == 1:
      return uniqueposs
    
    uniqueposs = possible.copy()
    
    #region
    regset = set([])
    for r in regneigh:
            if puzzle[r] == '.':
               regset = regset | dictionary[r]
               
    uniqueposs = uniqueposs - regset
    if len(uniqueposs) == 1:
      return uniqueposs
    
  return possible

  
def solve(puzzle, dictionary, nbrs, rown, coln, regn):
  #pre-process board
  for spot in dictionary:
    if puzzle[spot] == '.':
      possible = dictionary[spot]
      newposs = deduction(puzzle, spot, dictionary, possible, rown, coln, regn)
      if len(newposs) == 1:
        value = str(newposs.pop())
        puzzle[spot] = value
        dictionary[spot] = set()
        for indx in set(n for n in nbrs[spot] if puzzle[n] == '.'):
          if value in dictionary[indx]:
            dictionary[indx].remove(value)
   #base cases
  if '.' not in puzzle:
    if isSolved(puzzle):
      return puzzle
    return False    
 
  #find tile with least possibilities
  index = None
  smallest = 50

  for tile in dictionary:
      if puzzle[tile] == '.':
          if len(dictionary[tile]) < smallest:
              index = tile
              smallest = len(dictionary[tile])
  
  
  possible = dictionary[index]
  
  #if no possibilities, somethings wrong
  if len(possible) == 0:
    return False
  
  allneigh = set(n for n in nbrs[index] if puzzle[n] == '.')

  
  if len(possible) > 1:
    for neigh in allneigh:
        if puzzle[neigh] == '.':
            oneposs = dictionary[neigh]
            if len(oneposs) == 1:
                possible = possible - oneposs
                
  if len(possible) == 0:
    return False
  
  
  #brute force each possibility
  for x in possible:
    copy = {key:set(dictionary[key]) for key in dictionary}
    cpuzzle = list(puzzle)
    value = str(x)
    
    #remove the value from each of the neighbours possibilities
    broken = False
    
    for indx in allneigh:
      if value in copy[indx]:
        copy[indx].remove(value)

        #if a neighbour now has 0, somethings wrong, backtrack
        if len(copy[indx]) == 0:
          broken = True
          break
    if broken == True:
      continue
    
    cpuzzle[index] = value
    copy[index] = set()
    cpuzzle = solve(cpuzzle, copy, nbrs, rown, coln, regn)
    
    if cpuzzle != False:
      return cpuzzle
  return False    
  
  
  
  
import math
import copy
from time import time

sudoku = open('puzzles.txt').read().split()

totaltime = 0

neighbrs = {}

rownbrs = {}

colnbrs = {}

regnbrs = {}

for cell in range(81):
    row = findRowNbrs(cell)
    col = findColNbrs(cell)
    reg = findRegNbrs(cell)
    allnbrs = row + col + reg
    rownbrs[cell] = row
    colnbrs[cell] = col
    regnbrs[cell] = reg
    neighbrs[cell] = allnbrs

for x in range(len(sudoku)):
  test = sudoku[x]

  print("#%r" % (x+1), end="   ")
  print("")

  puzzle = []
  dictionary = {}
 
  for s in test:
    puzzle.append(s)
    
      
  for x in range(81):
    if puzzle[x] == '.':
      dictionary[x] = findPossibilites(puzzle, x)
      
  if isSolved(puzzle) == True:
    print("This is already solved.")
  else:
    tic = time()
    puzzle = solve(puzzle, dictionary, neighbrs, rownbrs, colnbrs, regnbrs)
    toc = time()
    print('Time = %f seconds' % ( toc - tic ) )
    totaltime += (toc - tic)
    
    
print('Total time = %f seconds' % (totaltime))


      

    
    
    

