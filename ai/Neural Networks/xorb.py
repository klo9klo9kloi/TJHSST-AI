def function(y):
  z = (1+(math.e**-y))**-1
  return z

def half(w, inpt):
  y1 = w[0] + (w[1]*inpt[0]) + (w[2]*inpt[1])
  y2 = w[3] + (w[4]*inpt[0]) + (w[5]*inpt[1])
  
  h1 = function(y1)
  h2 = function(y2)
 
  tup = (h1, h2)
  return tup
  
def run(w, inpt):
  y1 = w[0] + (w[1]*inpt[0]) + (w[2]*inpt[1])
  y2 = w[3] + (w[4]*inpt[0]) + (w[5]*inpt[1])
  
  
  h1 = function(y1)
  h2 = function(y2)
  
  
  y3 = w[6] + (w[7]*h1) + (w[8]*h2)

  z = function(y3)
 
  return z

def backpropupper(zs, testcases, hs, dw, w):
  calc = 0
  for case in testcases:
    z = zs[case]
    t = testcases[case]
    d = dw[case]
    h = hs[case]
    calc += ((z-t)*z*(1-z)*w*h*(1-h)*d)
  return calc

def backproplower(zs, testcases, dw):
  calc = 0
  for case in testcases:
    z = zs[case]
    t = testcases[case]
    d = dw[case]
    calc += ((z-t)*z*(1-z)*d)
  return calc
  
def error(w, testcases):
  calc = 0
  for case in testcases:
    calc += ((testcases[case] - run(w, case))**2)
  return 0.5*calc 

import math
import random
from time import time

testcases = {(0,0):0, (0,1):1, (1,0):1, (1,1):0}
w = [1, 1, -1, 1, -1, 1, 1, -1, -1]               #[-1, -1, 1, -1, 1, -1, -1, 1, 1], [1, 1, -1, 1, -1, 1, 1, -1, -1]
dw = .1
'''
while(error(w,testcases) > 10**-3):
  print(w)
  print(error(w,testcases))
  tup = half(w, (0,0))
  y1 = w[6] + (w[7]*tup[0]) + (w[8]*tup[1])
  z1 = function(y1)
  
  tup1 = half(w, (0,1))
  y2 = w[6] + (w[7]*tup1[0]) + (w[8]*tup1[1])
  z2 = function(y2)
  
  tup2 = half(w, (1,0))
  y3 = w[6] + (w[7]*tup2[0]) + (w[8]*tup2[1])
  z3 = function(y3)
  
  tup3 = half(w, (1,1))
  y4 = w[6] + (w[7]*tup3[0]) + (w[8]*tup3[1])
  z4 = function(y4)
  
  z = {(0,0):z1, (0,1):z2, (1,0):z3, (1,1):z4}
  bias = {(0,0):1, (0,1):1, (1,0):1, (1,1):1}
  h1 = {(0,0):tup[0], (0,1):tup1[0], (1,0):tup2[0], (1,1):tup3[0]}
  h2 = {(0,0):tup[1], (0,1):tup1[1], (1,0):tup2[1], (1,1):tup3[1]}
  x1 = {(0,0):0, (0,1):0, (1,0):1, (1,1):1}
  x2 = {(0,0):0, (0,1):1, (1,0):0, (1,1):1}
  
  dw1 = backpropupper(z, testcases, h1, bias, w[7])
  dw2 = backpropupper(z, testcases, h1, x1, w[7])
  dw3 = backpropupper(z, testcases, h1, x2, w[7])
  dw4 = backpropupper(z, testcases, h2, bias, w[8])
  dw5 = backpropupper(z, testcases, h2, x1, w[8])
  dw6 = backpropupper(z, testcases, h2, x2, w[8])
  dw7 = backproplower(z, testcases, bias)
  dw8 = backproplower(z, testcases, h1)
  dw9 = backproplower(z, testcases, h2)
  
  w[0] = w[0] - dw1
  w[1] = w[1] - dw2
  w[2] = w[2] - dw3
  w[3] = w[3] - dw4
  w[4] = w[4] - dw5
  w[5] = w[5] - dw6
  w[6] = w[6] - dw7
  w[7] = w[7] - dw8
  w[8] = w[8] - dw9
'''

done = False
while not done:
  w = random.sample(range(-10, 10), 9)
  tic = time()
  toc = time()
  while(error(w,testcases) > 10**-3) and (toc - tic < 10):
    toc = time()
    print(w)
    print(error(w,testcases))
    tup = half(w, (0,0))
    y1 = w[6] + (w[7]*tup[0]) + (w[8]*tup[1])
    z1 = function(y1)
    
    tup1 = half(w, (0,1))
    y2 = w[6] + (w[7]*tup1[0]) + (w[8]*tup1[1])
    z2 = function(y2)
    
    tup2 = half(w, (1,0))
    y3 = w[6] + (w[7]*tup2[0]) + (w[8]*tup2[1])
    z3 = function(y3)
    
    tup3 = half(w, (1,1))
    y4 = w[6] + (w[7]*tup3[0]) + (w[8]*tup3[1])
    z4 = function(y4)
    
    z = {(0,0):z1, (0,1):z2, (1,0):z3, (1,1):z4}
    bias = {(0,0):1, (0,1):1, (1,0):1, (1,1):1}
    h1 = {(0,0):tup[0], (0,1):tup1[0], (1,0):tup2[0], (1,1):tup3[0]}
    h2 = {(0,0):tup[1], (0,1):tup1[1], (1,0):tup2[1], (1,1):tup3[1]}
    x1 = {(0,0):0, (0,1):0, (1,0):1, (1,1):1}
    x2 = {(0,0):0, (0,1):1, (1,0):0, (1,1):1}
    
    dw1 = backpropupper(z, testcases, h1, bias, w[7])
    dw2 = backpropupper(z, testcases, h1, x1, w[7])
    dw3 = backpropupper(z, testcases, h1, x2, w[7])
    dw4 = backpropupper(z, testcases, h2, bias, w[8])
    dw5 = backpropupper(z, testcases, h2, x1, w[8])
    dw6 = backpropupper(z, testcases, h2, x2, w[8])
    dw7 = backproplower(z, testcases, bias)
    dw8 = backproplower(z, testcases, h1)
    dw9 = backproplower(z, testcases, h2)
    
    w[0] = w[0] - dw1
    w[1] = w[1] - dw2
    w[2] = w[2] - dw3
    w[3] = w[3] - dw4
    w[4] = w[4] - dw5
    w[5] = w[5] - dw6
    w[6] = w[6] - dw7
    w[7] = w[7] - dw8
    w[8] = w[8] - dw9
  if(error(w,testcases) < 10**-3):
    done = True
    
print("Done")  
print(w)
print(error(w, testcases))
for case in testcases:
  tup = half(w, case)
  print(case)
  print(tup)
  print(run(w, case))
