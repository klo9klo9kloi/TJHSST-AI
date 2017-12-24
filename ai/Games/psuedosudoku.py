#have puzzle and index and poss
#need to fill in all forced squares
#before finding one with least possibilities, do:
#fill in all dots with one possibility
#only square/two out of three rule

#for each dot
#its possibilities are now the union of the all the sets of possibilities of all its neighbouring dots

for x in range (0, 81):
  if puzzle[x] == '.':
    poss = findPossibilities(puzzle, x)
    set([poss])
    #for everything in its row
      if puzzle[somevariable] == '.' and len(poss) != 1:
         poss = findPossibilities(puzzle, somevariable) - poss
    if len(poss) == 1
      stop
    else
       #for everything in its col
         if puzzle[somevariable] == '.' and len(poss) != 1:
            poss = findPossibilities(puzzle, somevariable) - poss
       if len(poss) == 1
          stop
       else
          #for everything in its reg
            if puzzle[somevariable] == '.' and len(poss) != 1:
               poss = findPossibilities(puzzle, somevariable) - poss
    if len(poss) == 1
      puzzle[x] = poss[0]
