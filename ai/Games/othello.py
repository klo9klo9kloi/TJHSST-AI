from sys import argv
from sys import stdout
from time import time

theE = ' '
theX = '+'
theO = 'O'

def pr( x ) :
   print( x )       # index = 0 or 1 or ... or 63
   #
   stdout . flush() # so the moderator can see it
   
def ib( r , c ) :
   return 0 <= r < 8 and 0 <= c < 8
   
def wouldBracket( theboard , thepiece , r , c , dr , dc ) :
   theother = findotherpiece(thepiece)
   if ib( r + dr , c + dc ) :
      #
      j = ( r + dr ) * 8 + ( c + dc )
      #
      if theboard[j] == theother :
         #
         r += dr
         c += dc
         #
         while ib( r + dr , c + dc ) :
            #
            j = ( r + dr ) * 8 + ( c + dc )
            #
            if theboard[j] == thepiece : return True
            if theboard[j] == theE     : return False
            #
            r += dr
            c += dc
            #
         #
      #
   #
   return False

def thenBracket( theboard , thepiece , r , c , dr , dc ) :
   theother = findotherpiece(thepiece)
   j = ( r + dr ) * 8 + ( c + dc )
   #
   while theboard[j] != thepiece :
      #
      theboard[j] =  thepiece
      #
      r += dr
      c += dc
      #
      j = ( r + dr ) * 8 + ( c + dc )
      
def makeMove( theboard , thepiece , themove ) :
   copy = theboard.copy()
   r = themove // 8 # row
   c = themove %  8 # col
   #
   #          E   NE    N   NW    W   SW   S  SE
   drlist = [ 0 , -1 , -1 , -1 ,  0 ,  1 , 1 , 1 ]
   dclist = [ 1 ,  1 ,  0 , -1 , -1 , -1 , 0 , 1 ]
   #
   drc = zip( drlist , dclist )
   #
   for ( dr , dc ) in drc :
      #
      if wouldBracket( copy , thepiece , r , c , dr , dc ) :
         #
         thenBracket(  copy , thepiece , r , c , dr , dc )
         #
      #
   #
   copy[themove] = thepiece
   return copy

def findotherpiece(mypiece):
  if mypiece == theX:
    return theO
  return theX
      
def heuristic(myboard, mypiece):
  mine = [i for i, j in enumerate(myboard) if j == mypiece]
  h = 0
  if myboard[0] == mypiece:
    h+=10
  if myboard[7] == mypiece:
    h+=10
  if myboard[56] == mypiece:
    h+=10
  if myboard[63] == mypiece:
    h+=10
  h += len(mine)
  return h

def findAllPossible(myboard, mypiece):
   alist = []
   j = 0

   while j < 64 :
      #
      if myboard[j] == theE :
         r = j // 8 # row
         c = j %  8 # col
         #          E   NE    N   NW    W   SW   S  SE
         drlist = [ 0 , -1 , -1 , -1 ,  0 ,  1 , 1 , 1 ]
         dclist = [ 1 ,  1 ,  0 , -1 , -1 , -1 , 0 , 1 ]
         drc = zip( drlist , dclist )
        
         for ( dr , dc ) in drc :
            if wouldBracket( myboard , mypiece , r , c , dr , dc ) :
               alist . append( j )
               break
      j += 1


   return alist

def printBoard(myBoard):
  for x in range(0, 63, 8):
    string = ""
    for x2 in range(x, x+8):
      string += (myBoard[x2] + " ")
    print(string)
    print(" ")
    
def alphabeta(board, depth, a, b, maximizingPlayer, mypiece):
  poss = findAllPossible(board, mypiece)
  otherpiece = findotherpiece(mypiece)
  
  if depth == 0 or len(poss) == 0:
    tup = (heuristic(board, mypiece), -1)
    return tup
  if maximizingPlayer:
    v = (float("-inf"), -1)
    for child in poss:
      v = max(v, alphabeta(makeMove(board, mypiece, child), depth - 1, a, b, False, otherpiece))
      v = (v[0], child)
      a = max(a, v[0])
      if b <= a:
        break
    return v
  else:
    v = (float("inf"), -1)
    for child in poss:
      v = min(v, alphabeta(makeMove(board, mypiece, child), depth - 1, a, b, True, otherpiece))
      v = (v[0], child)
      b = min(b, v[0])
      if b <= a:
        break
    return v

def main( myboard , mypiece ) :
   #
   # myboard = list of 64 chars
   # mypiece =          1 char
   #
   # row-major order ...  8 x  8
   # zero-indexed    ...  0 - 63
   #
   # print out the index where we place "mypiece"
   #
   temp = 0
   playsleft = [i for i, j in enumerate(myboard) if j == theE]
   if len(playsleft) < 10:
     temp = alphabeta(myboard, len(playsleft), float("-inf"), float("inf") , True, mypiece)
   else:
     temp = alphabeta(myboard, 4, float("-inf"), float("inf") , True, mypiece)
   pr(temp[1])
   
def altmain( myboard, mypiece):
  maxyield = 0
  bestmove = -1
  for p in findAllPossible(myboard, mypiece):
    temp = makeMove(myboard, mypiece, p)
    count = points(temp, mypiece)
    if count > maxyield:
       maxyield = count
       bestmove = p
  pr(bestmove)
    

   

if len( argv ) == 3 :
   #
   myboard = argv[1] # 64 chars
   mypiece = argv[2] #  1 char
   #
   n = len( myboard )
   m = len( mypiece )
   #
   if n == 64 and m == 1 :
      #
      myboard = list( myboard )
      
      main( myboard , mypiece )
      #
   #
#

