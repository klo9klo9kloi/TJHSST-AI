def checkBoard(board):
  for x in range(0, len(board)):
    for y in range(x+1, len(board)):
      if (board[y] == board[x] + (y-x)) or (board[y] == board[x] - (y-x)):
        return False
  return True

def swap(board, first, second):
  temp = board[first]
  board[first] = board[second]
  board[second] = temp
  
def genRand(n):
  x = random.randint(0, n)
  y = random.randint(0, n)
  while x == y:
    x = random.randint(0, n)
    y = random.randint(0, n)
  tup = (x, y)
  return tup

def findH(board):
  h = 0
  for x in range(0, len(board)):
    for y in range(x+1, len(board)):
      if (board[y] == board[x] + (y-x)) or (board[y] == board[x] - (y-x)):
        h += 1
  return h

import random
from time import time

n = 32
b = n-1

step = []
limit = n*n*n

tic = time()
for x in range(100):
  board = [z for z in range(0, n)]
  random.shuffle(board)

  h = findH(board)
  newh = None

  tup = None
  steps = 0
  
  while checkBoard(board) == False:
    tup = genRand(b)
    temp = list(board)
    swap(temp, tup[0], tup[1])
    newh = findH(temp)
    
    tries = 0
    while newh >= h and tries < limit:     # > for 1.0 success B)
      tup = genRand(b)
      temp = list(board)
      swap(temp, tup[0], tup[1])
      newh = findH(temp)
      tries += 1     
      
    if tries >= limit:
      break 
    else: 
      swap(board, tup[0], tup[1])
      steps+=1
      h = newh
  
  if checkBoard(board) == True:
    step.append(steps)
    
toc = time()


print('Time = %f seconds' % ( toc - tic ) )
    
print('Success rate = ' + str(len(step)/100))

avg = 0
for val in step:
  avg += val
avg = avg/len(step)
print('Average steps = ' + str(avg))
    