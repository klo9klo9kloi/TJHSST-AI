##################################################
#
# Torbert, 18 December 2015
#
##################################################
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
theE = '.'
theX = '+'
theO = 'O'
#
fname = 'myprog.py'
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
def getMove( fname , theboard , thepiece ) :
   #
   # TODO - check if no possible move
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
   #
   # TO DO - error check... themove
   #
   #------------------------ END ---------------------#
   #
   # TO DO - default to random play
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
# TODO - display the board
# TODO - play the entire game
#
string = ""
for piece in theboard:
  string += piece
print(string)
thepiece = theX # first move
#
tic = time()
num = getMove( fname , theboard , thepiece )
toc = time()
#
print( num )
#
##################################################
#
# end of file
#
##################################################
