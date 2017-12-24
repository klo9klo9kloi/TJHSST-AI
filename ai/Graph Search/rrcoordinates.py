from pickle import dump

import math

romnodes = open('rrNodes.txt').read().split()

index = 0

coordinates = {}

range1 = math.floor(len(romnodes)/3)

for x in range(0, range1):
        position = romnodes[index]
        index = index + 1
        xcoord = (float)(romnodes[index])
        index = index + 1
        ycoord = (float)(romnodes[index])
        index = index + 1
        point = (xcoord, ycoord)
        coordinates[position] = point
    

fout = open('rrcoordinates.pkl', 'wb')
dump(coordinates, fout, protocol = 2)
fout.close()
