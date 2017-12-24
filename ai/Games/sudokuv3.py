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

def findAllNbrs(index):
  nbrs = []
  
  row = math.floor(index/9)
  col = index%9
  
  row2 = math.floor(row/3) * 3
  col2 = math.floor(col/3) * 3
  
  #row
  for c in range(9):
      if c != col:
#        if puzzle[row * 9 + c] == '.':
           nbrs.append(row * 9 + c)  
  #column
  for y in range (col, col+(9*9), 9):
      if y != (row * 9 + col):
#        if puzzle[y] == '.':
           nbrs.append(y)
           
  #region
  for r in range (row2, row2+3):
      for co in range (col2, col2+3):
        position = r * 9 + co
        if position != (row * 9 + col):
#          if puzzle[position] == '.':
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

def deduction(index, dictionary, possible, rown, coln, regn):
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
  #base cases
  if isSolved(puzzle):
    #printMatrix(puzzle)
    return True
  if '.' not in puzzle:
    return False
  '''
  forced = []
  forcedchanges = []

  #fill in forced moves
  for til in range(81):
    if puzzle[til] == '.':
      if len (dictionary[til]) > 1:
        unique = deduction(til, dictionary, dictionary[til], rown, coln, regn)
        if len(unique) == 1:
          for only in unique:
            val = str(only)
            puzzle[til] = val
            forced.append(til)
            itsneigh = nbrs[til]
            
            for dot in itsneigh:
              if puzzle[dot] == '.':
                old = dictionary[dot]
                tup = (dot, dictionary[dot].copy())
                if val in old:
                  old.remove(val)
                  forcedchanges.append(tup)
                  
                  if len(old) == 0:
                    for c in forced:
                      puzzle[c] = '.'
                    for pair in forcedchanges:
                      indx = pair[0]
                      dictionary[indx] = pair[1]
                    return False
                  
             
                dictionary[dot] = old
  '''            
 
  #find tile with least possibilities
  index = None
  smallest = 50

  for tile in range(81):
      if puzzle[tile] == '.':
          if len(dictionary[tile]) < smallest:
              index = tile
              smallest = len(dictionary[tile])
  '''
  if index == None:
    solve(puzzle, dictionary)
  '''
  possible = dictionary[index]

  #if no possibilities, somethings wrong
  if len(possible) == 0:
    '''
    for forcedtiles in forced:
      puzzle[forcedtiles] = '.'
    for forcedneigh in forcedchanges:
      indx = forcedneigh[0]
      dictionary[indx] = forcedneigh[1]
#      puzzle[indx] = '.'    
    '''
    return False
  
  #find all its empty neighbours
  allneigh = nbrs[index]
  
  #deductions
  possible = deduction(index, dictionary, possible, rown, coln, regn)
  
  if len(possible) > 1:
    for neigh in allneigh:
        if puzzle[neigh] == '.':
            oneposs = dictionary[neigh]
            if len(oneposs) == 1:
                possible = possible - oneposs
                
  if len(possible) == 0:
    '''
    for forcedtiles in forced:
      puzzle[forcedtiles] = '.'
    for forcedneigh in forcedchanges:
      indx = forcedneigh[0]
      dictionary[indx] = forcedneigh[1]
#      puzzle[indx] = '.'
    '''
    return False
  
  #brute force each possibility
  for x in possible:
    value = str(x)
    puzzle[index] = value

    #track changed tiles
    changed = []
    broken = False
    
    #remove the value from each of the neighbours possibilities
    for indx in allneigh:
        if puzzle[indx] == '.':
          itsposs = dictionary[indx]
          tup = (indx, dictionary[indx].copy())
          if value in itsposs:
            itsposs.remove(value)
            changed.append(tup)
            
            #if a neighbour now has 0, somethings wrong, backtrack
            if len(itsposs) == 0:
               for tup in changed:
                  indx = tup[0]
                  dictionary[indx] = tup[1]
               broken = True
               break
             
          
          #give its updated possibilities
          dictionary[indx] = itsposs
          
        '''
        for c in range(9):
          if c != col:
            if puzzle[row * 9 + c] == '.':
              thoseposs = dictionary[row * 9 + c]
              tup = (row * 9 + c, dictionary[row*9+c].copy())       
              if value in thoseposs:
                 thoseposs.remove(value)
                 changed.append(tup)
                 
              if len(thoseposs) == 0:
                  return False
              if len(thoseposs) == 1:
                  only = thoseposs.pop()
                  puzzle[row * 9 + c] = only
                  changed.append(row * 9 + c)
                  
              dictionary[row * 9 + c] = thoseposs               
        for y in range (col, col+(9*9), 9):
          if y != (row * 9 + col):
            if puzzle[y] == '.':
              thoseposs1 = dictionary[y]
              back2 = (y, dictionary[y].copy())
              if value in thoseposs1:
                 thoseposs1.remove(value)
                 changed.append(back2)
              
              if len(thoseposs1) == 0:
                  return False
              if len(thoseposs1) == 1:
                  only = thoseposs1.pop()
                  puzzle[y] = only
                  changed.append(y)
             
              dictionary[y] = thoseposs1 
        row2 = math.floor(row/3) * 3
        col2 = math.floor(col/3) * 3
      
        for r in range (row2, row2+3):
          for co in range (col2, col2+3):
            position = r * 9 + co
            if position != (row * 9 + col):
              if puzzle[position] == '.':
                thoseposs2 = dictionary[position]
                back3 = (position, dictionary[position].copy())
                if value in thoseposs2:
                  thoseposs2.remove(value)
                  changed.append(back3)
                
                if len(thoseposs2) == 0:
                  return False
                if len(thoseposs2) == 1:
                  only = thoseposs2.pop()
                  puzzle[position] = only
                  changed.append(position)
                  
                dictionary[position] = thoseposs2
                '''
    if broken == True:
      puzzle[index] = '.'
      continue
    
    if solve(puzzle, dictionary, nbrs, rown, coln, regn) == True:
      return True
    else:
      puzzle[index] = '.'
      for tup in changed:
          indx = tup[0]
          dictionary[indx] = tup[1]
#          puzzle[indx] = '.'
  '''
  for forcedtiles in forced:
    puzzle[forcedtiles] = '.'
  for forcedneigh in forcedchanges:
    indx = forcedneigh[0]
    dictionary[indx] = forcedneigh[1]
#    puzzle[indx] = '.'
  '''
  
  
  return False  
  
  
  
  
import math
from time import time

sudoku = open('sudoku128.txt').read().split()

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

for x in range(128):
  test = sudoku[x]

  print("#%r" % (x+1), end="   ")
  print("")
  printMatrix(test)

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
    solve(puzzle, dictionary, neighbrs, rownbrs, colnbrs, regnbrs)
    toc = time()
    print('Time = %f seconds' % ( toc - tic ) )
    printMatrix(puzzle)
    totaltime += (toc - tic)
    
    
print('Total time = %f seconds' % (totaltime))


      

    
    
    

