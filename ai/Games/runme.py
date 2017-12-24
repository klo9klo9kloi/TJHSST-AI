#!/usr/bin/python3
#
# Torbert, 18 December 2015
#
# chmod 755 runme.py
#
# ./runme.py
#
##################################################
#
from random     import choice
#
from subprocess import Popen
from subprocess import PIPE
from subprocess import TimeoutExpired
#
from time       import time
#
##################################################
#
TIMEOUT = 1.5 # seconds allowed per move
#
theE = ' '
theX = '+'
theO = 'O'
#
fname = 'othello.py'
gname = 'myprog.py'
#
##################################################
#
def st( alist ) :
   #
   return '' . join( alist )
   #
#
##################################################
#
def ib( r , c ) :
   #
   return 0 <= r < 8 and 0 <= c < 8
   #
#
##################################################
#
def wouldBracket( theboard , thepiece , r , c , dr , dc ) :
   #
   theother = theX
   #
   if theother == thepiece : theother = theO
   #
   #
   #
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
   #
#
##################################################
#
def thenBracket( theboard , thepiece , r , c , dr , dc ) :
   #
   theother = theX
   #
   if theother == thepiece : theother = theO
   #
   #
   #
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
      #
   #
#
##################################################
#
def getPossMoves( theboard , thepiece ) :
   #
   alist = []
   #
   j = 0
   #
   while j < 64 :
      #
      if theboard[j] == theE :
         #
         r = j // 8 # row
         c = j %  8 # col
         #
         #          E   NE    N   NW    W   SW   S  SE
         drlist = [ 0 , -1 , -1 , -1 ,  0 ,  1 , 1 , 1 ]
         dclist = [ 1 ,  1 ,  0 , -1 , -1 , -1 , 0 , 1 ]
         #
         drc = zip( drlist , dclist )
         #
         for ( dr , dc ) in drc :
            #
            if wouldBracket( theboard , thepiece , r , c , dr , dc ) :
               #
               alist . append( j )
               #
               break
               #
            #
      #
      j += 1
      #
   #
   return alist
   #
#
##################################################
#
def getMove( fname , theboard , thepiece ) :
   #
   possMoves = getPossMoves( theboard , thepiece )
   #
   if len( possMoves ) == 0 : return -1 # does happen
   #
   #------------------------ RUN THE PLAYER'S CODE ---#
   #
   strboard = st( theboard )
   #
   myargs = [ 'python3' , fname , strboard , thepiece ]
   #
   po = Popen( myargs , stdout = PIPE , stderr = PIPE )
   #
   # import io
   # print( 'io' , io.DEFAULT_BUFFER_SIZE ) # 8192
   #
   try :
      #
      x , y = po . communicate( timeout = TIMEOUT )
      #
   except TimeoutExpired :
      #
      po . kill()
      #
      x , y = po . communicate()
      #
      print( '*** timeout' )
      #
   #
   z = x . split()
   #
   if len( z ) > 0 :
      #
      themove = z[-1] . decode( 'utf-8' ) # last only
      #
      print( '*** themove' , themove )
      #
      # check for a match with zero-indexed moves
      #
      print( '*** zero' )
      #
      for move in possMoves :
         #
         if ( '%d' % move ) == themove : return move
         if ('+%d' % move ) == themove : return move
         #
      #
      # then check for a one-indexed (OBOB) match
      #
      print( '*** obob' )
      #
      for move in possMoves :
         #
         move1 = move + 1
         #
         if ( '%d' % move1 ) == themove : return move
         if ('+%d' % move1 ) == themove : return move
         #
      #
      # then check for a row-column OBOB move too
      #
      print( '*** obob rowcol' )
      #
      for move in possMoves :
         #
         r = move // 8 # row ... zero-indexed
         c = move %  8 # col
         #
         r += 1 # one-indexed = OBOB = off-by-one-bug
         c += 1
         #
         j = r * 8 + c
         #
         if ( '%d' % j ) == themove : return move
         if ('+%d' % j ) == themove : return move
         #
      #
   #
   #------------------------ END ---------------------#
   #
   print( '*** default random' )
   #
   return choice( possMoves ) # default = random play
   #
#
##################################################
#
def makeMove( theboard , thepiece , themove ) :
   #
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
      if wouldBracket( theboard , thepiece , r , c , dr , dc ) :
         #
         thenBracket(  theboard , thepiece , r , c , dr , dc )
         #
      #
   #
   theboard[themove] = thepiece
   #
#
##################################################
#
def pr( x ) :
   #
   print()
   #
   nums = '01234567'
   #
   print( ' ' , end = ' ' )
   print( ' ' , end = ' ' )
   print( ' ' + '_' * ( 2 * len( nums ) + 1 ) + ' ' ) # top _ underscore
   #
   for r in nums :
      #
      print( ' ' , end = ' ' )
      print(  r  , end = ' ' )
      print( '|' , end = ' ' )
      #
      for c in nums :
         #
         j = int(r) * 8 + int(c)
         #
         print( x[j] , end = ' ' )
         #
      #
      print( '|' , end = ' ' )
      print( r )
      #
   #
   print( ' ' , end = ' ' )
   print( ' ' , end = ' ' )
   print( ' ' + '-' * ( 2 * len( nums ) + 1 ) + ' ' ) # bottom - dash
   #
   print( ' ' , end = ' ' )
   print( ' ' , end = ' ' )
   print( ' ' , end = ' ' )
   #
   for c in nums :
      #
      print( c , end = ' ' )
      #
   #
   print()
   print()
   #
#
##################################################
#
theboard = [ theE ] * 64
#
theboard[27] = theX
theboard[36] = theX
theboard[28] = theO
theboard[35] = theO
#
pr( theboard )
#
theother = theO
thepiece = theX # first move
#
oldnum = 0
#
while True :
   #
   print( '*' * 50 )
   #
   tic = time()
   num = getMove( fname , theboard , thepiece )
   toc = time()
   #
   if num != -1 :
      #
      print( thepiece , fname )
      print( 'num' , num )
      print( 'row' , num // 8 )
      print( 'col' , num %  8 )
      print( 'sec' , toc - tic )
      #
      makeMove( theboard , thepiece , num )
      #
      pr( theboard )
      #
      print( '%c =' % theX , theboard . count( theX ) )
      print( '%c =' % theO , theboard . count( theO ) )
      #
      print()
      #
   else :
      #
      if oldnum == -1 : break
      #
   #
   oldnum = num
   #
   thepiece , theother = theother , thepiece
   fname    , gname    = gname    , fname
   #
#
##################################################
#
# end of file
#
##################################################
