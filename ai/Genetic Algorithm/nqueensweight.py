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

def findH(board, weights):
  h = 0
  for x in range(0, len(board)):
    for y in range(x+1, len(board)):
      if (board[y] == board[x] + (y-x)) or (board[y] == board[x] - (y-x)):
        h += (weights[y] * weights[x])
  return h

from random import shuffle

n = 8

step = []

weights = [4,1,1,4,4,1,1,4]

for x in range(100):
  board = [x for x in range(0, n)]
  shuffle(board)

  h = findH(board, weights)

  minh = 100000
  tup = None
  steps = 0
  while checkBoard(board) == False:
    for x in range(0, len(board)):
      for y in range(x+1, len(board)):
        temp = list(board)
        swap(temp, x, y)
        calc = findH(temp, weights)
        if calc < minh:
           minh = calc
           tup = (x, y)  
    if minh < h:
      swap(board, tup[0], tup[1])
      steps+=1
      h = minh
    else:
      break
  if checkBoard(board) == True:
    step.append(steps)
    
    
print('Success rate = ' + str(len(step)/100))

avg = 0
for val in step:
  avg += val
avg = avg/len(step)
print('Average steps = ' + str(avg))
    