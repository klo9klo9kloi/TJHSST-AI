from math import atan2
from collections import Counter
import math

#starting image
img = open('me.ppm').read().split()
height = img[1]
width = img[2]
string = "" + height + " " + width + "\n"


#gray


output = open('gray.ppm', 'w')
output.write('P3\n')
output.write(string)
output.write('255\n')
for x in range(4, len(img), 3):
  gray = str(int(0.3 * float(img[x]) + 0.59 * float(img[x+1]) + 0.11 * float(img[x+2])))
  output.write(gray + ' ')
  output.write(gray + ' ')
  output.write(gray + ' ')
output.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#blur

img = open('gray.ppm').read().split()

matrix = [[0 for x in range(int(height))] for x in range(int(width))] 
indx = 4
for lol in range(0, len(matrix)):
  for xd in range(0, len(matrix[0])):
    matrix[lol][xd] = (img[indx], img[indx+1], img[indx+2])
    indx += 3

outputb = open('blur.ppm', 'w')
outputb.write('P3\n')
outputb.write(string)
outputb.write('255\n')

for colin in range(0, len(matrix)):
  for numan in range(0, len(matrix[0])):
    if colin == 0 or numan == 0 or colin == (len(matrix)-1) or numan == (len(matrix[0])-1):
      tup = matrix[colin][numan]
      outputb.write(tup[0] + ' ')
      outputb.write(tup[1] + ' ')
      outputb.write(tup[2] + ' ')
    else:
      tup = matrix[colin][numan]
      tupt = matrix[colin-1][numan]
      tupb = matrix[colin+1][numan]
      tupl = matrix[colin][numan-1]
      tupr = matrix[colin][numan+1]
      tuptl = matrix[colin-1][numan-1]
      tuptr = matrix[colin-1][numan+1]
      tupbl = matrix[colin+1][numan-1]
      tupbr = matrix[colin+1][numan+1]
      avgr = (float(tup[0]) + float(tupt[0]) + float(tupb[0]) + float(tupl[0]) + float(tupr[0]) + float(tuptl[0]) + float(tuptr[0]) + float(tupbl[0]) + float(tupbr[0]))/9
      avgb = (float(tup[1]) + float(tupt[1]) + float(tupb[1]) + float(tupl[1]) + float(tupr[1]) + float(tuptl[1]) + float(tuptr[1]) + float(tupbl[1]) + float(tupbr[1]))/9
      avgg = (float(tup[2]) + float(tupt[2]) + float(tupb[2]) + float(tupl[2]) + float(tupr[2]) + float(tuptl[2]) + float(tuptr[2]) + float(tupbl[2]) + float(tupbr[2]))/9
      outputb.write(str(int(avgr)) + ' ')
      outputb.write(str(int(avgb)) + ' ')
      outputb.write(str(int(avgg)) + ' ')


outputb.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#edge detection

threshold = 50   #175 for cwar

imge = open('blur.ppm').read().split()

matrix = [[0 for x in range(int(height))] for x in range(int(width))] 
gstore = [[0 for x in range(int(height))] for x in range(int(width))]
astore = [[0 for x in range(int(height))] for x in range(int(width))]
edges = {}
thinned = {}

edgecount1 = 0

indx = 4
for lol in range(0, len(matrix)):
  for xd in range(0, len(matrix[0])):
    matrix[lol][xd] = img[indx]
    indx += 3

output = open('edges.ppm', 'w')
output.write('P3\n')
output.write(string)
output.write('255\n')

for colin in range(0, len(matrix)):
  for numan in range(0, len(matrix[0])):
    if colin == 0 or numan == 0 or colin == (len(matrix)-1) or numan == (len(matrix[0])-1):
      output.write(matrix[colin][numan] + ' ')
      output.write(matrix[colin][numan] + ' ')
      output.write(matrix[colin][numan] + ' ')
    else:
      tup = float(matrix[colin][numan])
      tupt = float(matrix[colin-1][numan])
      tupb = float(matrix[colin+1][numan])
      tupl = float(matrix[colin][numan-1])
      tupr = float(matrix[colin][numan+1])
      tuptl = float(matrix[colin-1][numan-1])
      tuptr = float(matrix[colin-1][numan+1])
      tupbl = float(matrix[colin+1][numan-1])
      tupbr = float(matrix[colin+1][numan+1])
      
      
      mask1 = (-1*tuptl) + (0*tupt) + (1*tuptr) + (-2*tupl) + (0*tup) + (2*tupr) + (-1*tupbl) + (0*tupb) + (1*tupbr)
      mask2 = (-1*tuptl) + (-2*tupt) + (-1*tuptr) + (0*tupl) + (0*tup) + (0*tupr) + (1*tupbl) + (2*tupb) + (1*tupbr)
      
      g = (abs(mask1) + abs(mask2))
      
      if g > threshold:
        output.write('255 ')
        output.write('0 ')
        output.write('0 ')
        
        edgecount1 += 1
        
        gstore[colin][numan] = g
        
        tup = (colin, numan)
        
        angle = atan2(mask1, mask2)
        astore[colin][numan] = angle
        
        edges[tup] = 0
      else:
        #output.write(matrix[colin][numan] + ' ')
        #output.write(matrix[colin][numan] + ' ')
        #output.write(matrix[colin][numan] + ' ')
        output.write('255 ')
        output.write('255 ')
        output.write('255 ')

output.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#thin

edgecount2 = 0

img2 = open('edges.ppm').read().split()

matrix2 = [[0 for x in range(int(height))] for x in range(int(width))] 

indx = 4
for lol in range(0, len(matrix2)):
  for xd in range(0, len(matrix2[0])):
    matrix2[lol][xd] = img2[indx]
    indx += 3
   

output2 = open('thin.ppm', 'w')
output2.write('P3\n')
output2.write(string)
output2.write('255\n')



for colin in range(0, len(matrix2)):
  for numan in range(0, len(matrix2[0])):
    tup = (colin, numan)
    if tup in edges:    #175 for cwar
      
        angle = astore[colin][numan]
        g = gstore[colin][numan]
        remove = False
        
        if g > threshold:
          if (angle <= math.pi and angle > 7*(math.pi/8)) or (angle < (math.pi/8) and angle > -math.pi/8) or (angle >= -math.pi and angle < -7*(math.pi/8)):
            g1 = gstore[colin-1][numan]
            g2 = gstore[colin+1][numan]
            if g < g1 and g < g2:
              remove = True
          elif (angle < 7*(math.pi/8) and angle > 5*(math.pi/8)) or (angle < -math.pi/8 and angle > -3*(math.pi/8)):
            g1 = gstore[colin-1][numan+1]
            g2 = gstore[colin+1][numan-1]
            if g < g1 and g < g2:
              remove = True
          elif (angle < 5*(math.pi/8) and angle > 3*(math.pi/8)) or (angle > -5*(math.pi/8) and angle < -3*(math.pi/8)):
            g1 = gstore[colin][numan+1]
            g2 = gstore[colin][numan-1]
            if g < g1 and g < g2:
              remove = True
          elif (angle < 3*(math.pi/8) and angle > (math.pi/8)) or (angle > -7*(math.pi/8) and angle < -5*(math.pi/8)):
            g1 = gstore[colin-1][numan-1]
            g2 = gstore[colin+1][numan+1]
            if g < g1 and g < g2:
              remove = True
        
        if remove == True:
          output2.write('255 ')
          output2.write('255 ')
          output2.write('255 ')
          gstore[colin][numan] = 0
          thinned[tup] = 0
        else:
          output2.write('255 ')
          output2.write('0 ')
          output2.write('0 ')
          edgecount2 += 1
          
        
    else:
      output2.write(matrix2[colin][numan] + ' ')
      output2.write(matrix2[colin][numan] + ' ')
      output2.write(matrix2[colin][numan] + ' ')
      
      
        
      
        
output2.close()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#canny

edgecount3 = 0
img3 = open('thin.ppm').read().split()

matrix3 = [[0 for x in range(int(height))] for x in range(int(width))]

indx = 4
for lol in range(0, len(matrix3)):
  for xd in range(0, len(matrix3[0])):
    matrix3[lol][xd] = img3[indx]
    indx += 3
   

output3 = open('canny.ppm', 'w')
output3.write('P3\n')
output3.write(string)
output3.write('255\n')

high = 150

for colin in range(0, len(matrix3)):
  for numan in range(0, len(matrix3[0])):
    tup = (colin, numan)
    if tup in edges and tup not in thinned:
      angle = astore[colin][numan] + (math.pi/2)
      if angle > math.pi:
        angle = angle - math.pi
      g = gstore[colin][numan]
      
      edge1 = None
      edge2 = None
      keep = True
      
      if (angle <= math.pi and angle > 7*(math.pi/8)) or (angle < (math.pi/8) and angle > -math.pi/8) or (angle >= -math.pi and angle < -7*(math.pi/8)):
          edge1 = gstore[colin-1][numan]
          edge2 = gstore[colin+1][numan]

      elif (angle < 7*(math.pi/8) and angle > 5*(math.pi/8)) or (angle < -math.pi/8 and angle > -3*(math.pi/8)):
          edge1 = gstore[colin-1][numan+1]
          edge2 = gstore[colin+1][numan-1]
            
      elif (angle < 5*(math.pi/8) and angle > 3*(math.pi/8)) or (angle > -5*(math.pi/8) and angle < -3*(math.pi/8)):
          edge1 = gstore[colin][numan+1]
          edge2 = gstore[colin][numan-1]
          
      elif (angle < 3*(math.pi/8) and angle > (math.pi/8)) or (angle > -7*(math.pi/8) and angle < -5*(math.pi/8)):
          edge1 = gstore[colin-1][numan-1]
          edge2 = gstore[colin+1][numan+1]
          
      if g < high:
        if edge2 > high or edge1 > high:
          keep = True
        else:
          keep = False
      if keep == True:
        output3.write('255 ')
        output3.write('0 ')
        output3.write('0 ')
        edgecount3 += 1
      else:
        output3.write('255 ')
        output3.write('255 ')
        output3.write('255 ')
        gstore[colin][numan] = 0
        thinned[tup] = 0
        
        
          
    else:
       output3.write('255 ')
       output3.write('255 ')
       output3.write('255 ')
       
output3.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#hough 
 
votes = [[0 for x in range(int(height))] for x in range(int(width))]
radii = {}

for s in range(0, len(votes)):
  for x in range(0, len(votes[0])):
    tup = (s,x)
    radii[tup] = []

output4 = open('hough.ppm', 'w')
output4.write('P3\n')
output4.write(string)
output4.write('255\n')

maxvote = 0

for edge in edges:
  if edge not in thinned:
    angle = astore[edge[0]][edge[1]]
    
    start1 = edge[0]
    start2 = edge[1]
    xc = start1
    yc = start2
    radius = 1
    while xc > 0 and yc > 0 and yc < (int(height)-1) and xc < (int(width)-1):
      xc = start1 + (radius*math.cos(angle)) 
      yc = start2 + (radius*math.sin(angle))
      tup = (int(xc), int(yc))
      votes[int(xc)][int(yc)] += 1
      radii[tup].append(radius)
      val = votes[int(xc)][int(yc)]
      if val > maxvote:
        maxvote = val
      radius += 1
    radius = 1
    xc = start1
    yc = start2
    while xc > 0 and yc > 0 and yc < (int(height)-1) and xc < (int(width)-1):
      xc = start1 - (radius*math.cos(angle)) 
      yc = start2 - (radius*math.sin(angle))
      tup = (int(xc), int(yc))
      votes[int(xc)][int(yc)] += 1
      radii[tup].append(radius)
      val = votes[int(xc)][int(yc)]
      if val > maxvote:
        maxvote = val
      radius += 1
      
grayincrement = 255/maxvote

centers = {}
nextcenter = None

for flash in range(0, len(votes)):
  for jaygarrick in range(0, len(votes[0])):
    gray = str(255 - int(votes[flash][jaygarrick] * grayincrement))
    if votes[flash][jaygarrick] == maxvote:
      nextcenter = (flash, jaygarrick)
      tup = nextcenter
      centers[tup] = 0
    output4.write(gray + ' ')
    output4.write(gray + ' ')
    output4.write(gray + ' ')
    
output4.close()



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#find circles

outline = {}
radi = {}

nextmax = maxvote

while nextmax > (maxvote * .95):
  
  centers[nextcenter] = 0
  
  radiusfind = Counter(radii[nextcenter])
  most = radiusfind.most_common(1)
  radi[nextcenter] = most[0][0]
  radius = most[0][0]
  
  for barry in range(0, len(votes)):
    for allen in range(0, len(votes[0])):
      dist = int(math.sqrt(math.pow((barry-nextcenter[0]),2) + math.pow((allen-nextcenter[1]),2)))
      tup = (barry, allen)
      if dist == radius and tup not in outline:
          outline[tup] = nextcenter
  
  temp = 0
  loc = None
  
  for cap in range(0, len(votes)):
    for tony in range(0, len(votes[0])):
      tup = (cap, tony)
      if votes[cap][tony] > temp and tup not in centers:
        temp = votes[cap][tony]
        loc = tup 
        
  nextmax = temp
  nextcenter = loc

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#draw circles


img5 = open('blur.ppm').read().split()

matrix5 = [[0 for x in range(int(height))] for x in range(int(width))]

indx = 4
for lol in range(0, len(matrix5)):
  for xd in range(0, len(matrix5[0])):
    matrix5[lol][xd] = img5[indx]
    indx += 3

output5 = open('circleguess.ppm', 'w')
output5.write('P3\n')
output5.write(string)
output5.write('255\n')

for batman in range(0, len(matrix5)):
  for superman in range(0, len(matrix5[0])):
    tup = (batman, superman)
    if tup in centers:
      output5.write('255 ')
      output5.write('20 ')
      output5.write('147 ')
    elif tup in outline:
      output5.write('255 ')
      output5.write('20 ')
      output5.write('147 ')
    else:
      output5.write(matrix5[batman][superman] + ' ')
      output5.write(matrix5[batman][superman] + ' ')
      output5.write(matrix5[batman][superman] + ' ')
output5.close()



          
          
          
          
          
          
          
          
          
          
          
          
          
          
          