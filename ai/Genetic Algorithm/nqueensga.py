def checkBoard(board):
  for x in range(0, len(board)):
    for y in range(x+1, len(board)):
      if (board[y] == board[x] + (y-x)) or (board[y] == board[x] - (y-x)):
        return False
  return True

def swap(board, first, second):
  temp = board[first]
  board[first] = board[second]
  board[second] = temp

def mutate(child):
  board = child
  h = findH(board)

  minh = 100000
  tup = None
  
  while checkBoard(board) == False:
    for x in range(0, len(board)):
      for y in range(x+1, len(board)):
        temp = list(board)
        swap(temp, x, y)
        calc = findH(temp)
        if calc < minh:
           minh = calc
           tup = (x, y)  
    if minh < h:
      swap(board, tup[0], tup[1])
      h = minh
    else:
      break
  return board


def splyce(first, second, n):
  index = random.randint(1, n-2)
  child1 = []
  child2 = []
  for x in range(0, n):
    if x < index:
      child1.append(first[x])
      child2.append(second[x])
    else:
      child2.append(first[x])
      child1.append(second[x])
  chance = random.randint(0, 100)
  if chance > 70:
    child = random.randint(1, 2)
    if child == 1:
      child1 = mutate(child1)
    else:
      child2 = mutate(child2)
  tup1 = (child1, findH(child1))
  tup2 = (child2, findH(child2))
  tup = (tup1, tup2)
  return tup
  

def findH(board):              
  h = 0
  for x in range(0, len(board)):
    for y in range(x+1, len(board)):
      if (board[y] == board[x] + (y-x)) or (board[y] == board[x] - (y-x)):
        h += 1
      if (board[y] == board[x]):
        h += 1
  return h

def avg(population):
  score = 0
  for organism in population:
    score += organism[1]
  return int(score/len(population))

def killavg(population, avg):
  newpop = []
  for organism in population:
    if organism[1] <= avg:
      newpop.append(organism)
  return newpop

def check(population):
  for organism in population:
    score = organism[1]
    if score == 0:
      return organism
  return False

def stagnated(population, popsize):
  scores = []
  for organism in population:
    kind = organism[0]
    score = 0
    for others in population:
      if others[0] == kind:
        score += 1
    scores.append(score)
  for s in scores:
    if s > (popsize/2):
      return True
  return False

import random
from random import shuffle
from time import time
from operator import itemgetter

n = 8
popsize = n * 4

found = False

population = []


for x in range(popsize):
  newboard = [0,1,2,3,4,5,6,7]
  shuffle(newboard)
  tup = (newboard, findH(newboard))
  population.append(tup)

  
print('Start:')
print(population)

tic = time()  

loops = 0  
while(check(population) == False) and stagnated(population, popsize) == False:
  newpop = []
  count = 0
  temp = sorted(population, key= itemgetter(1))
  
  while count < popsize:
    first = random.randint(0, n)
    second = random.randint(0, n)
    while second == first:
      second = random.randint(0, n)
    temp1 = temp[first]
    temp2 = temp[second]
    children = splyce(temp1[0], temp2[0], n)
    if children[0] not in newpop:
      newpop.append(children[0])
      count += 1
    if children[1] not in newpop:
      newpop.append(children[1])
      count += 1
  

  population = list(newpop)
  loops += 1
  
toc = time()

 
print(population)
print(check(population))
print(loops) 

print('Time = %f seconds' % ( toc - tic ) )


  
