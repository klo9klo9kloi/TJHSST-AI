def countUnhappy(board, empty):
  count = 0
  for x in range(0, len(board)):
    if board[x] != empty:
      temp = calc(board, x, board[x], empty)
      if temp == 0:
        count += 1
  return count

def printBoard(board):
  print("")
  for y in range(1, len(board)+1):
    if y%8 == 0:
      print(board[y-1])
    else:
      print(board[y-1], end="")

def calc(board, x, piece, empty):
  same = 0
  empt = 0
  up = x - 8
  down = x + 8
  left = x - 1
  right = x + 1
  tl = x - 9
  tr = x - 7
  bl = x + 7
  br = x + 9
  
  h = 0
  
  if up >= 0:
    if board[up] == piece:
      same += 1
    elif board[up] == empty:
      empt += 1
  else:
    empt += 1
    
  if down < 64:
    if board[down] == piece:
      same += 1
    elif board[down] == empty:
      empt += 1
  else:
    empt += 1
    
  if x%8 != 0:
    if board[left] == piece:
      same += 1
    elif board[left] == empty:
      empt += 1
  else:
    empt += 1
    
  if x%8 != 7:
    if board[right] == piece:
      same += 1
    elif board[right] == empty:
      empt += 1
  else:
    empt += 1
    
  if tl > 0:
    if board[tl] == piece:
      same += 1
    elif board[tl] == empty:
      empt += 1
  else:
    empt += 1
    
  if tr >= 0:
    if board[tr] == piece:
      same += 1
    elif board[tr] == empty:
      empt += 1
  else:
    empt += 1
    
  if bl < 64:
    if board[bl] == piece:
      same += 1
    elif board[bl] == empty:
      empt += 1
  else:
    empt += 1
    
  if br < 64:
    if board[br] == piece:
      same += 1
    elif board[br] == empty:
      empt += 1
  else:
    empt += 1
    
  if empt < 3:
    h = 3
  elif empt < 6:
    h = 2
  else:
    h = 1
  
  if same >= h:
    return 1
  else:
    return 0
  
import random

board = []
n = 8

white = ".."
black = "><"
empty = '  '


for x in range(0, n*n):
  if x%2 == 0:
    board.append(black)
  else:
    board.append(white)
    
    
removed = [0, 7, 56, 63]

board[0] = empty
board[7] = empty
board[56] = empty
board[63] = empty



for x in range(0, 20):
  pos = random.randint(0, 63)
  while pos in removed:
    pos = random.randint(0, 63)
  board[pos] = empty
  removed.append(pos)
  
printBoard(board)
  

while countUnhappy(board, empty) != 0:
  for x in range(0, len(board)):
    if board[x] != empty and calc(board, x, board[x], empty) == 0:
      pos = random.choice(removed)
      board[pos] = board[x]
      board[x] = empty
      removed.remove(pos)
      removed.append(x)

  
printBoard(board)

    
    
