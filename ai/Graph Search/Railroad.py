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

graph = load(open('rr.pkl', 'rb'))
coordinates = load(open('rrcoordinates.pkl', 'rb'))


shortest = []

cost = 0

setsize = 0


target = input("Enter start: ")
destination = input("Enter end: ")

tic = time()

findInfo(target, destination, graph, coordinates)

toc = time() 

print(shortest)
print(cost)
print('Time = %f seconds' % ( toc - tic ) )
print(setsize)