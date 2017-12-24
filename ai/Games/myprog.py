##################################################
#
# Torbert, 18 December 2015
#
##################################################
#
from sys import argv
from sys import stdout
#
##################################################
#
def pr( x ) :
   #
   print( x )       # index = 0 or 1 or ... or 63
   #
   stdout . flush() # so the moderator can see it
   #
#
##################################################
#
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
   pr(  0 ) # corner at the top-left
   pr(  7 ) # corner at the top-right
   pr( 63 ) # corner at the bottom-right
   pr(  0 )
   pr(  0 ) # only the last-printed move is made
   #
#
##################################################
#
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
      #
      main( myboard , mypiece )
      #
   #
#
##################################################
#
# end of file
#
##################################################
