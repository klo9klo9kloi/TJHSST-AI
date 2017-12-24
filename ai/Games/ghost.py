def givePoss(word, wordlist):
  #primitive
  possible = []
  size = len(word)
  for strings in wordlist:
    string = strings[:size]
    if word == string:
      possible.append(strings)
  if len(possible) == 0:
    return "" 
  hints = []
  for poss in possible:
    letter = poss[size: size+1]
    if letter not in hints:
      hints.append(letter)
  if len(hints) > 0:
    return sorted(hints)
  return "Tough luck"

def cheat(word, wordlist, turnnumber, numplay):
  if word in wordlist:
    if len(word)%numplay == turnnumber:
      return True
    else:
      return False
  possible = givePoss(word, wordlist)
  cheats = []
  for poss in possible:
    attempt = word + poss
    returned = cheat(attempt, wordlist, turnnumber, numplay)
    if returned != False:
      cheats.append(poss)
  if len(cheats) != 0:
    return cheats
  return False
  

words = open('ghost.txt').read().split()
wordlist = {}

for word in words:
  wordlist[word] = None
  
print("")  
print("Welcome to Ghost!")
print("")

num = int(input('Number of players? '))
print("")


players = {}
names = {}
turns = []

for x in range(0, num):
  player = input('Enter name: ')
  names[x] = player
  players[x] = 0
  turns.append(x)

word = ""

print("")


#finish fixing moderator program. you need to be able to remove players from play
while len(players) != 1:
   letter = ""
   rotation = turns.pop(0)
   displayed = names[rotation]
   letter = input('%s:  ' % displayed)
   
   if len(letter) > 1:
     print('Enter only one letter')
     turns.insert(0, rotation)
     continue
   if letter == ' ' or letter == '':
     print('Please enter a letter')
     turns.insert(0, rotation)
     continue
   if letter == '!':
     if word in wordlist:
       #other person gets a letter
       prevplayer = turns[len(turns)-1]
       players[prevplayer] += 1
       word = ""
       turns.insert(0, rotation)
     else:
       #you get a letter
       players[rotation] += 1
       word = ""     
     print("")
     print("STATUS")
     print("------")
     for player in players:
       ghost = ""
       if players[player] == 0:
         pass
       if players[player] == 1:
         ghost = "G"
       if players[player] == 2:
         ghost = "GH"
       if players[player] == 3:
         ghost = "GHO"
       if players[player] == 4:
         ghost = "GHOS"
       if players[player] == 5:
         ghost = "GHOST"
       print('%s: %s' % (names[player], ghost))
     print("------")
     print("")
   elif letter == '?':
     hint = givePoss(word, wordlist)
     cheat = cheat(word, wordlist, rotation+1)
     print("")
     print("Possible: %s" % hint)
     print("Cheat: %s" % cheat)
     print("")
     turns.insert(0, rotation)
   else: 
     letter = letter.lower()
     word += letter
     print("Word: %s" % word)
     print("")
     
   pop = None  
   for player in players:
     if players[player] == 5:
       pop = player
       print(pop)
   if pop != None:
     players.pop(pop, None)
     print("")
     print("*****************")
     print("%s got GHOSTED!" % names[pop])
     print("*****************")
     print("")
   else:
     if rotation not in turns:
       turns.append(rotation)


for player in players:
  print('Player %i wins!' % (player+1))


     

