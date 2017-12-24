class Node(object):
    def __init__ (self, value):
        self.value     = value  # is either a lower-case letter or a '$'
        self.children  = {}     # Example: {'a':Node('a'), 'b':Node('b'), etc.}


    def __repr__(self): # Both node.print() and print(node) call the same code.
        self.print()
        return ''


    def print(self, stng): # recursively print All words
        if self.value == '$':
            print (stng[:-1]) # The -1 will avoid printing the '$'.
            return
        for ch in self.children:
            stngCopy = stng + ch
            self.children[ch].print(stngCopy) # recursive call

    def display(self, level):    #  This is a (recursive) utility used for for debugging.
        if self.value == '$': return

     #--print data
        print ('========== NODE ========== level =', level)
        print ('--> self.value     =', self.value)
        print ('--> self.children: [', end = '')

      #--print values of node's children
        for key in self.children:
            if key != '$':
               print (key, sep ='', end = ', ')
        print (']')
        print()

     #--RECURSIVELY print the node's children
        for char in self.children:
            level += 1
            (self.children[char]).display(level)

    def insert(self, stng): # recursive

    #---case 1. Insert termination character '$'
        if stng == '':
           self.children['$'] = Node('$')
           return

    #--case 2. If the initial character (stng[0]) is NOT one of the children, then insert the character
    #          into the children dictionary and recurse with the remainder of the string.
        if stng[0] not in self.children:
           p = Node(stng[0])
           self.children[stng[0]] = p
           p.insert(stng[1:])

    #--case 3. Since stng[0] is already in the children dictionary, recurse and insert the rest of the string.
        self.children[stng[0]].insert(stng[1:])

    def search(self, stng): # recursive
        #--case 1. final letter is found in trie
           if len(stng) == 0:
              if '$' in self.children:
                 return True
              else:
                 return False
        #--case 2. current letter in not in trie
           if stng[0] not in self.children:
               return False

        #--case 3. go on  to look at the next letter.
           return self.children[stng[0]].search (stng[1:])

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

def wouldLose(possplay, wordlist, turn):
  if wordlist.search(possplay) == True:
    if len(possplay)%2 == turn:
      return True
    else:
      return False
  possible = givePoss(possplay, wordlist)
  narrowed = narrow(possplay, wordlist)
  count = 0
  for poss in possible:
    attempt = possplay + poss
    returned = wouldLose(attempt, narrowed, turn)
    if returned != True:
      count += 1
  if count >= (len(wordlist)/2):
    return False
  return True
  
  

def computer(word, wordlist, key, turn):
  if wordlist.search(word) == True:
    return '!'
  
  possible = primitive(word, key)
  #narrowed = narrow(word, wordlist)
  
  newposs = []
  newposs1 = []
  #prevent immediate loss
  for ch in possible:
    maybe = word+ch
    if maybe in key:
      continue
    newposs.append(ch)
    
  #would lose
  for cha in newposs:
    possplay = word+cha
    if wouldLose(possplay, wordlist, turn) == False:
       newposs1.append(cha)
       
  if len(newposs1) == 0:
    if len(newposs) == 0:
      return choice(possible)
    return choice(newposs)
  
  return choice(newposs1)




from random import choice

words = open('ghost.txt').read().split()
wordlist = Node('*')
key = {}

for wrd in words:
  wordlist.insert(wrd)
  key[wrd] = None
  

print("")  
print("Welcome to Ghost!")
print("")
name = input("Please enter your name: ")
print("")

word = ""
ghost = {}
ghost[0] = 0
ghost[1] = 0
players = {}
players[0] = name
players[1] = "Computer"

turn = 0

winner = None

letters = {}
makeLetters(letters)

while(True):
  letter = ""
  displayed = players[turn]
  if turn == 0:  
    letter = input('%s:  ' % displayed)
    letter = letter.lower()
  else:
    letter = computer(word, wordlist, key, turn)
    print('%s: %s' % (displayed, letter))
  
  if letter not in letters:
    print('Please enter a valid letter.')
    continue
  if letter == '!':
    if wordlist.search(word) == True:
       #other person gets a letter
       prevplayer = (turn+1) % 2
       ghost[prevplayer] += 1
       word = ""
       turn = (turn+1) % 2
    elif playable(word, wordlist) == False:
       prevplayer = (turn+1) % 2
       ghost[prevplayer] += 1
       word = ""
       turn = (turn+1) % 2
    else:
       #you get a letter
       ghost[turn] += 1
       word = ""     
    print("")
    print("STATUS")
    print("------")
    for player in ghost:
       ghosts = ""
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
       print('%s: %s' % (players[player], ghosts))
    print("------")
    print("")
  elif letter == '?':
     hint = givePoss(word, wordlist)
     #cheat = cheat(word, wordlist, rotation+1)
     print("")
     print("Possible: %s" % hint)
     #print("Cheat: %s" % cheat)
     print("")
     turns.insert(0, rotation)
  else: 
     word += letter
     print("Word: %s" % word)
     print("")
  
  finish = False
  for player in ghost:
    if ghost[player] == 5:
      winner = (player+1) % 2
      finish = True
  if finish == True:
    break
  turn = (turn+1) % 2
  
  
print("%s Wins!" % (players[winner]))      
  
  
  