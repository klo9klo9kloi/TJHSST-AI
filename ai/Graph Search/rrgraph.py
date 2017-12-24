def calc(current, end):
   y1  = float(current[0])
   x1  = float(current[1])
   y2  = float(end[0])
   x2  = float(end[1])
   #
   R   = 3958.76 # miles
   #
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   #
   # approximate great circle distance with law of cosines
   #
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R




from pickle import dump

from math import pi , acos , sin , cos

import math

rrnodes = open('rrNodes.txt').read().split()

index = 0

coordinates = {}

range1 = math.floor(len(rrnodes)/3)

for x in range(0, range1):
        position = rrnodes[index]
        index = index + 1
        xcoord = (float)(rrnodes[index])
        index = index + 1
        ycoord = (float)(rrnodes[index])
        index = index + 1
        point = (xcoord, ycoord)
        coordinates[position] = point



rrEdges = open('rrEdges.txt').read().split()

part = 1

previous = None

edges = {}

for x in rrEdges:
  edges[x] = {}

for s in rrEdges:
     if part == 1:
          previous = s
          part = 2
     else:
          distance = (calc(coordinates[s], coordinates[previous]))
          
          list1 = edges[previous]
          list2 = edges[s]
          
          list1[s] = distance
          list2[previous] = distance

          part = 1
          
          
#for y in edges:
#  print(y)
#  print(edges[y])
          
fout = open('rr.pkl', 'wb')
dump(edges, fout, protocol = 2)
fout.close()
