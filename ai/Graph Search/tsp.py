def findDist(plot):
  prev = 0
  d = 0
  for x in range(0, len(plot)):
    first = plot[x]
    second = plot[prev]
    d += math.sqrt(math.pow(first[0]-second[0], 2) + math.pow(first[1]-second[1], 2))
    prev = x
  return d

def genRand(n):
  x = random.randint(0, n)
  y = random.randint(0, n)
  while x == y:
    x = random.randint(0, n)
    y = random.randint(0, n)
  tup = (x, y)
  return tup

def swap(board, first, second):
  temp = board[first]
  board[first] = board[second]
  board[second] = temp

import math
import random
from math import atan2

points = open('tsp0038.txt').read().split()

xctr = 42813.3406421
yctr = 11735.8260211


plot = []

num = int(points[0])
count = 1

for o in range(1, num*2, 2):
  x = points[o]
  y = points[o+1]
  tup = (float(x), float(y), atan2( float(y) - yctr , float(x) - xctr ), count)
  plot.append(tup)
  count+=1
  

plot.sort(key=lambda tup: tup[2])



dist = findDist(plot)
bestd = 1000000
tup = None

steps = 0


while(True):
  for x in range(0, len(plot)):
      for y in range(x+1, len(plot)):
        temp = list(plot)
        swap(temp, x, y)
        calc = findDist(temp)
        if calc < bestd:
           bestd = calc
           tup = (x, y)  
  if bestd < dist:
      swap(plot, tup[0], tup[1])
      steps+=1
      dist = bestd
  else:
      break

'''
n = 38
b = n-1

step = []
limit = n*n*n


  
while(True):
  tup = genRand(b)
  temp = list(plot)
  swap(temp, tup[0], tup[1])
  newd = findDist(temp)
    
  tries = 0
  while newd > dist and tries < limit:     # > for 1.0 success B)
    tup = genRand(b)
    temp = list(plot)
    swap(temp, tup[0], tup[1])
    newd = findDist(temp)
    tries += 1     
      
  if tries >= limit:
    break 
  else: 
    swap(plot, tup[0], tup[1])
    dist = newd
'''
    
print(dist)
temp = []
for tup in plot:
  temp.append(tup[3])
print(temp)
  

    