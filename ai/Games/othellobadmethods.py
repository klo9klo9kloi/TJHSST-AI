def flip(myboard, move, otherpiece, mypiece):
  bound = move - (move%8)
  re = myboard.copy()
  if ( move - 1 > bound):
    temp = move - 1
    while(re[temp] == otherpiece):
      temp -= 1
    if(re[temp] == mypiece):
      for x in range(temp+1, move):
         re[x] = mypiece
  #check right
  bound = (move + 8) - ((move+8)%8) - 1
  if ( move + 1 < bound):
    temp = move + 1
    while(re[temp] == otherpiece):
      temp += 1
    if(re[temp] == mypiece):
      for x in range(move+1, temp):
        re[x] = mypiece
  #check up
  bound = move%8
  if ( move - 8 > bound):
    temp = move - 8
    while(re[temp] == otherpiece):
      temp -= 8
    if(re[temp] == mypiece):
      for x in range(temp+8, move, 8):
        re[x] = mypiece
  #check down
  bound = 63 - (move%8)
  if ( move + 8 < bound):
    temp = move + 8
    while(re[temp] == otherpiece):
      temp += 8
    if(re[temp] == mypiece):
      for x in range(move+8, temp, 8):
        re[x] = mypiece
  #check northwest
  bound = move - ((move%8)*9)
  if ( move - 9 > bound):
    temp = move - 9
    while(re[temp] == otherpiece):
      temp -= 9
    if(re[temp] == mypiece):
      for x in range(temp+9, move, 9):
        re[x] = mypiece
  #check northeast
  bound = move - ((move%8)*7)
  if ( move - 7 > bound):
    temp = move - 7
    while(re[temp] == otherpiece):
      temp -= 7
    if(re[temp] == mypiece):
      for x in range(temp+7, move, 7):
        re[x] = mypiece
  #check southeast
  bound = move + ((move%8)*9)
  if ( move + 9 < bound):
    temp = move + 9
    while(re[temp] == otherpiece):
      temp += 9
    if(re[temp] == mypiece):
      for x in range(move+9, temp, 9):
        re[x] = mypiece
  #check southwest
  bound = move + ((move%8)*7)
  if ( move + 7 < bound):
    temp = move + 7
    while(re[temp] == otherpiece):
      temp += 7
    if(re[temp] == mypiece):
      for x in range(move+7, temp, 7):
        re[x] = mypiece
  return re

def potentialyield(myboard, move, otherpiece, mypiece):
  gain = 0
  #check left
  bound = move - (move%8)
  if ( move - 1 > bound):
    temp = move - 1
    temp1 = 0
    while(myboard[temp] == otherpiece):
      temp1 += 1
      temp -= 1
    if(myboard[temp] == mypiece):
      gain += temp1
  #check right
  bound = (move + 8) - ((move+8)%8) - 1
  if ( move + 1 < bound):
    temp = move + 1
    temp1 = 0
    while(myboard[temp] == otherpiece):
      temp1 += 1
      temp += 1
    if(myboard[temp] == mypiece):
      gain += temp1
  #check up
  bound = move%8
  if ( move - 8 > bound):
    temp = move - 8
    temp1 = 0
    while(myboard[temp] == otherpiece):
      temp1 += 1
      temp -= 8
    if(myboard[temp] == mypiece):
      gain += temp1
  #check down
  bound = 63 - (move%8)
  if ( move + 8 < bound):
    temp = move + 8
    temp1 = 0
    while(myboard[temp] == otherpiece):
      temp1 += 1
      temp += 8
    if(myboard[temp] == mypiece):
      gain += temp1
  #check northwest
  bound = move - ((move%8)*9)
  if ( move - 9 > bound):
    temp = move - 9
    temp1 = 0
    while(myboard[temp] == otherpiece):
      temp1 += 1
      temp -= 9
    if(myboard[temp] == mypiece):
      gain += temp1
  #check northeast
  bound = move - ((move%8)*7)
  if ( move - 7 > bound):
    temp = move - 7
    temp1 = 0
    while(myboard[temp] == otherpiece):
      temp1 += 1
      temp -= 7
    if(myboard[temp] == mypiece):
      gain += temp1
  #check southeast
  bound = move + ((move%8)*9)
  if ( move + 9 < bound):
    temp = move + 9
    temp1 = 0
    while(myboard[temp] == otherpiece):
      temp1 += 1
      temp += 9
    if(myboard[temp] == mypiece):
      gain += temp1
  #check southwest
  bound = move + ((move%8)*7)
  if ( move + 7 < bound):
    temp = move + 7
    temp1 = 0
    while(myboard[temp] == otherpiece):
      temp1 += 1
      temp += 7
    if(myboard[temp] == mypiece):
      gain += temp1
      
  return gain