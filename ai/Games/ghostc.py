def makeLetters(letters):
  letters['a'] = None
  letters['b'] = None
  letters['c'] = None
  letters['d'] = None
  letters['e'] = None
  letters['f'] = None
  letters['g'] = None
  letters['h'] = None
  letters['i'] = None
  letters['j'] = None
  letters['k'] = None
  letters['l'] = None
  letters['m'] = None
  letters['n'] = None
  letters['o'] = None
  letters['p'] = None
  letters['q'] = None
  letters['r'] = None
  letters['s'] = None
  letters['t'] = None
  letters['u'] = None
  letters['v'] = None
  letters['w'] = None
  letters['x'] = None
  letters['y'] = None
  letters['z'] = None
  letters['!'] = None
  letters['?'] = None

def playable(word, wordlist):
  possible = []
  size = len(word)
  for strings in wordlist:
    string = strings[:size]
    if word == string:
      possible.append(strings)
  if len(possible) == 0:
    return False
  return True

def narrow(word, wordlist):
  if word == "":
    return wordlist
  possible = {}
  size = len(word)
  for strings in wordlist:
    string = strings[:size]
    if word == string:
      possible[strings] = None
  return possible

def cheat(word, wordlist, turn, num):
  if word in wordlist:
    return '!'
  possible = primitive(word, wordlist)
  if num == 2:
    narrowed = narrow(word, wordlist)
    
    newposs1 = []

    for ch in possible:
      possplay = word+ch
      if tryToWin(possplay, narrowed, (turn+1) % 2) == False:
        newposs1.append(ch)
    
    if len(newposs1) == 0:
      return possible
    return newposs1
  else:
    newposs1 = []
    for ch in possible:
      attempt = word+ch
      if attempt not in wordlist:
        newposs1.append(ch)
    if len(newposs1) == 0:
      return possible
    return newposs1
    

def primitive(word, wordlist):
  possible = []
  size = len(word)
  for strings in wordlist:
    string = strings[:size]
    if word == string:
      possible.append(strings)
  if len(possible) == 0:
    return "!"
  hints = []
  for poss in possible:
    letter = poss[size: size+1]
    if letter not in hints:
      hints.append(letter)
  if len(hints) > 0:
    return sorted(hints)
  return "!"

def givePoss(word, wordlist):
  possible = []
  size = len(word)
  for strings in wordlist:
    string = strings[:size]
    if word == string:
      possible.append(strings)
  if len(possible) == 0:
    return possible
  hints = []
  for poss in possible:
    letter = poss[size: size+1]
    if letter not in hints:
      hints.append(letter)
  if len(hints) > 0:
    return sorted(hints)
  return possible

def wouldWin(possplay, wordlist, turn):
  if possplay in wordlist:
    if len(possplay)%2 == turn:
      return True
    else:
      return False
  possible = givePoss(possplay, wordlist)
  narrowed = narrow(possplay, wordlist)
  for poss in possible:
    attempt = possplay + poss
    returned = wouldWin(attempt, narrowed, (turn+1) % 2)
    if returned == False:
      return True   
  return False

def tryToWin(possplay, wordlist, turn):
  if possplay in wordlist:
    if len(possplay)%2 == turn:
      return True
    else:
      return False
  possible = givePoss(possplay, wordlist)
  narrowed = narrow(possplay, wordlist)
  wins = 0
  losses = 0
  for poss in possible:
    attempt = possplay + poss
    returned = tryToWin(attempt, narrowed, (turn+1) % 2)
    if returned == False:
      wins += 1
    else:
      losses += 1
  if wins > losses:
    return True
  return False

def computer(word, wordlist, turn):
  if word in wordlist:
    return '!'
  possible = primitive(word, wordlist)
  narrowed = narrow(word, wordlist)
  
  newposs1 = []

  for ch in possible:
    possplay = word+ch
    if wouldWin(possplay, narrowed, (turn+1) % 2) == False:
      newposs1.append(ch)
  print(newposs1)
  if len(newposs1) == 0:
    return choice(possible)
  return choice(newposs1)



from random import choice

words = open('ghost.txt').read().split()
wordlist = {}

for wrd in words:
  wordlist[wrd] = None
  
print("")  
print("Welcome to Ghost!")
print("")
ai = input("Play against computer? (Yes/No)  " )
print("")

ghost = {}

players = {}

num = 2

if ai == 'No':
  num = int(input("Enter number of players: "))
  print("")
  for x in range (num):
    name = input("Please enter your name: ")
    players[x] = name
    ghost[name] = 0
    print("")
    
if ai == 'Yes':
  name = input("Please enter your name: ")
  players[1] = name
  players[0] = "Computer"
  ghost[name] = 0
  ghost["Computer"] = 0


word = ""

playing = 0
previous = None

winner = None

letters = {}
makeLetters(letters)


#fix turn system. if computer wins and starts the turn, the calculation still bases it on playing 2nd

while(True):
  letter = ""
  displayed = players[playing]
  
  if displayed == "Computer":  
    letter = computer(word, wordlist, playing)
    print('%s: %s' % (displayed, letter))
  else:
    letter = input('%s:  ' % displayed)
    letter = letter.lower() 
  
  if letter not in letters:
    print('Please enter a valid letter.')
    continue
  
  if letter == '!':
    if word in wordlist:
       #other person gets a letter
       prevplayer = players[previous]
       ghost[prevplayer] += 1
       word = ""
       
       readd = []
       readd.append(displayed)
       
       rotato = (playing+1) % num
       while rotato != playing:
         if players[rotato] != prevplayer:
           readd.append(players[rotato])
         rotato = (rotato+1) % num
       
       readd.append(prevplayer)
       
       for order in players:
         players[order] = readd.pop(0)
             
    elif playable(word, wordlist) == False:
       prevplayer = players[previous]
       ghost[prevplayer] += 1
       word = ""
       
       readd = []
       readd.append(displayed)
       
       rotato = (playing+1) % num
       while rotato != playing:
         if players[rotato] != prevplayer:
           readd.append(players[rotato])
         rotato = (rotato+1) % num
       
       readd.append(prevplayer)
       
       for order in players:
         players[order] = readd.pop(0)
    else:
       #you get a letter
       ghost[displayed] += 1
       word = ""
       
       readd = []
       
       rotato = (playing+1) % num
       
       while rotato != playing:
           readd.append(players[rotato])
           rotato = (rotato+1) % num
       
       readd.append(displayed)
       
       for order in players:
         players[order] = readd.pop(0)
       
       
    print("")
    print("STATUS")
    print("------")
    for p in players:
       ghosts = ""
       player = players[p]
       if ghost[player] == 0:
         pass
       if ghost[player] == 1:
         ghosts = "G"
       if ghost[player] == 2:
         ghosts = "GH"
       if ghost[player] == 3:
         ghosts = "GHO"
       if ghost[player] == 4:
         ghosts = "GHOS"
       if ghost[player] == 5:
         ghosts = "GHOST"
       print('%s: %s' % (player, ghosts))
    print("------")
    print("")
    
    playing = 0
    previous = None
    
  elif letter == '?':
     cheats = cheat(word, wordlist, playing, num)
     print("")
     print("Possible: %s" % cheats)
     print("")
     
  else: 
     word += letter
     print("Word: %s" % word)
     print("")
     previous = playing
     playing = (playing+1) % num
  
  topop = None
  for player in ghost:
    if ghost[player] == 5:
      topop = player
      
  if topop != None:
    ghost.pop(topop, None)
    print("%s TURNED TO THE DARK SIDE!" % topop)
    print("")
    readd = []
    for playing in players:
      name = players[playing]
      if name in ghost:
        readd.append(name)
        
    players = {}
    
    for x in range(len(ghost)):
      players[x] = readd.pop(0)
    num = num-1
    playing = (playing+1) % num
    
  if len(ghost) == 1:
    break
  
  

print("%s Wins!" % (players[0]))      
  
  
  
