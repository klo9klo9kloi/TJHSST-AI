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
  
def error(w, testcases):
  calc = 0
  for case in testcases:
    calc += ((testcases[case] - run(w, case))**2)
  return 0.5*calc 

import math

testcases = {(0,0):0, (0,1):1, (1,0):1, (1,1):0}
w = [1, 1, 1, 1, 1, 1, 1, 1, 1]
dw = .1

while(error(w,testcases) > 10**-1):
  print(w)
  errorr = error(w, testcases)
  print(errorr)
  w0 = list(w)
  w1 = list(w)
  w2 = list(w)
  w3 = list(w)
  w4 = list(w)
  w5 = list(w)
  w0[0] = w0[0] + dw
  w1[1] = w1[1] + dw
  w2[2] = w2[2] + dw
  w3[3] = w3[3] + dw
  w4[4] = w4[4] + dw
  w5[5] = w5[5] + dw
  error0 = error(w0, testcases)
  error1 = error(w1, testcases)
  error2 = error(w2, testcases)
  error3 = error(w3, testcases)
  error4 = error(w4, testcases)
  error5 = error(w5, testcases)
  
  
  
  d1 = (error0 - errorr)/dw
  d2 = (error1 - errorr)/dw
  d3 = (error2 - errorr)/dw
  d4 = (error3 - errorr)/dw
  d5 = (error4 - errorr)/dw
  d6 = (error5 - errorr)/dw
  
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
  
  
  dw7 = ((z1 - 0)*(1 - z1)*z1) + ((z2 - 1)*(1 - z2)*z2) + ((z3 - 1)*(1 - z3)*z3) + ((z4 - 0)*(1 - z4)*z4)
  dw8 = ((z1 - 0)*(1 - z1)*z1*tup[0]) + ((z2 - 1)*(1 - z2)*z2*tup1[0]) + ((z3 - 1)*(1 - z3)*z3*tup2[0]) + ((z4 - 0)*(1 - z4)*z4*tup3[0])
  dw9 = ((z1 - 0)*(1 - z1)*z1*tup[1]) + ((z2 - 1)*(1 - z2)*z2*tup1[1]) + ((z3 - 1)*(1 - z3)*z3*tup2[1]) + ((z4 - 0)*(1 - z4)*z4*tup3[1])
  
  w[0] = w[0] - d1
  w[1] = w[1] - d2
  w[2] = w[2] - d3
  w[3] = w[3] - d4
  w[4] = w[4] - d5
  w[5] = w[5] - d6
  w[6] = w[6] - dw7
  w[7] = w[7] - dw8
  w[8] = w[8] - dw9
  
print("Done")  
print(w)
print(error(w, testcases))
for case in testcases:
  tup = half(w, case)
  print(tup)
  print(run(w, case))
