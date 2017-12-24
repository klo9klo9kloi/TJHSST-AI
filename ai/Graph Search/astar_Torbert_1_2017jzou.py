def findInfo(start, end, dict, values):

    pqueue = []
    
    seen = {}
    parents = {}
    
    closed = {}
    
    seen[start] = 0
    parents[start] = None
    
    starttuple = (0, start)
    
    heappush(pqueue, starttuple)
    
    endpoint = values[end]
    
    
    while len(pqueue) != 0:           
        node = heappop(pqueue)
        
        position = node[1]
        
        if position not in closed:
            closed[position] = None
        
        distance = seen[position]
        
        if position == end:
            break
        else:
            neighbourlist = dict[position]
            for neighbour in neighbourlist:
                newdistance = neighbourlist[neighbour]
                total = distance + newdistance
                if neighbour not in seen:    
                    seen[neighbour] = total
                    parents[neighbour] = position
                         
                    point = values[neighbour]
                    
                    newtuple = (seen[neighbour] + calc(point, endpoint), neighbour)
                    heappush(pqueue, newtuple)
                elif total < seen[neighbour]: 
                    seen[neighbour] = total
                    parents[neighbour] = position
                    
                    point = values[neighbour]
                    
                    newtuple = (seen[neighbour] + calc(point, endpoint), neighbour)
                    heappush(pqueue, newtuple)
		    


    
    global shortest    
    shortest = findPath(parents, start, end)
    
    global cost
    cost = node[0]
    
    global setsize
    setsize = len(closed)

    
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
 

def findPath(parents, start, end):
    pathqueue = Queue()
    tempqueue = LifoQueue()
   
    pathqueue.put(end)
    
    
    while pathqueue.empty() == False:
        pathpart = pathqueue.get()
        if pathpart == start:
            break
        tempqueue.put(pathpart)
        pathqueue.put(parents[pathpart])
    
    finallist = []
    finallist.append(start)
    while tempqueue.empty() == False:
        finallist.append(tempqueue.get())
    
    return finallist
    


from pickle import load

from time import time

from queue import Queue, LifoQueue 

from heapq import heappush, heappop

from math import pi , acos , sin , cos

import math

nodes = open('nodes.txt').read().split()

index = 0

coordinates = {}

range1 = math.floor(len(nodes)/3)

for x in range(0, range1):
        position = nodes[index]
        index = index + 1
        xcoord = (float)(nodes[index])
        index = index + 1
        ycoord = (float)(nodes[index])
        index = index + 1
        point = (xcoord, ycoord)
        coordinates[position] = point


edges = open('edges.txt').read().split()

part = 1

previous = None

graph = {}

for x in edges:
  graph[x] = {}

for s in edges:
     if part == 1:
          previous = s
          part = 2
     else:
          distance = (calc(coordinates[s], coordinates[previous]))
          
          list1 = graph[previous]
          list2 = graph[s]
          
          list1[s] = distance
          list2[previous] = distance

          part = 1
          


shortest = []

cost = 0

setsize = 0

puzzle = open('puzzle.txt').read().split()

for x in range(0, len(puzzle), 2):
    target = puzzle[x]
    destination = puzzle[x+1]
    findInfo(target, destination, graph, coordinates)
    print(cost)
    print(setsize)
    print()

