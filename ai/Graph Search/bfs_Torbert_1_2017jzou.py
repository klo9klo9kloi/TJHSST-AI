def findInfo(start, end, dict):
  
    queue = Queue()
    nextlevel = Queue()
    lvl = {}
    parents = {}
    
    level = 1
    
    lvl[start] = 0
    parents[start] = None
    
    nextlevel.put(start)
    queue.put(nextlevel)
    
    found = False
    
    
    while queue.empty() == False:
        current = queue.get()

        nextlevel = Queue()
        while current.empty() == False:
            node = current.get()
            if node == end:
                found = True
                break
            else:
                for neighbour in dict[node]:
                    if neighbour not in lvl:
                        lvl[neighbour] = level
                        parents[neighbour] = node
                        nextlevel.put(neighbour)
        if found == True:
            break
        queue.put(nextlevel)
        level = level + 1
    
    global shortest    
    shortest = findPath(parents, start, end)
    global edges
    edges = findLevel(lvl, end)
    
    
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

def findLevel(level, end):
    return level[end]
    

from pickle import load

from time import time

from queue import Queue, LifoQueue 

dictionary = load(open('neigh.pkl', 'rb'))

shortest = []

edges = 0


puzzle =  open('puzzle.txt').read().split()

for x in range(0, len(puzzle), 2):
  target = puzzle[x]
  destination = puzzle[x+1]
  findInfo(target, destination, dictionary)
  print(shortest)
  print(edges)
  print()
  





