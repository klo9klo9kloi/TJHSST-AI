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

def findH(board):
  h = 0
  for x in range(0, len(board)):
    for y in range(x+1, len(board)):
      if (board[y] == board[x] + (y-x)) or (board[y] == board[x] - (y-x)):
        h += 1
  return h

from random import shuffle

n = 69

board = [x for x in range(0, n)]
shuffle(board)

h = findH(board)
print('First board = ' + str(board))
print('First h =' + str(h))


minh = 100000
tup = None

while checkBoard(board) == False:
  for x in range(0, len(board)):
    for y in range(x+1, len(board)):
      #if (board[y] == board[x] + (y-x)) or (board[y] == board[x] - (y-x)):
        temp = list(board)
        swap(temp, x, y)
        calc = findH(temp)
        print('Temp =' + str(temp))
        print('Temph =' + str(calc))
        if calc < minh:
          minh = calc
          tup = (x, y)  
  if minh < h:
    swap(board, tup[0], tup[1])
    h = minh
    print('Swapped board = ' + str(board))
  else:
    break
  
print(board)
print(findH(board))
print(checkBoard(board))