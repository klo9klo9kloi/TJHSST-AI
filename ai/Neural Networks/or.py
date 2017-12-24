def function(y):
  z = (1+(math.e**-y))**-1
  return z

def error(w0, w1, w2, testcases):
  error = 0
  for case in testcases:
    y = w0 + (w1*case[0]) + (w2*case[1])
    error = error + ((testcases[case] - function(y))**2)
  return 0.5*error 

import math

testcases = {(0,0):0, (0,1):1, (1,0):1, (1,1):1}

w0 = 0
w1 = 0
w2 = 0

dw = .1

'''
while(error(w0,w1,w2,testcases) > 10**-6):
  print(w0)
  print(w1)
  print(w2)
  errorr = error(w0, w1, w2, testcases)
  error0 = error(w0 + dw, w1, w2, testcases)
  error1 = error(w0, w1 + dw, w2, testcases)
  error2 = error(w0, w1, w2 + dw, testcases)
  
  d1 = (error0 - errorr)/dw
  d2 = (error1 - errorr)/dw
  d3 = (error2 - errorr)/dw
  
  w0 -= (0.8*d1)
  w1 -= (0.8*d2)
  w2 -= (0.8*d3)
'''

while(error(w0,w1,w2,testcases) > 10**-6):
  print(w0)
  print(w1)
  print(w2)
  y1 = w0 + (w1*0) + (w2*0)
  y2 = w0 + (w1*0) + (w2*1)
  y3 = w0 + (w1*1) + (w2*0)
  y4 = w0 + (w1*1) + (w2*1)
  
  z1 = function(y1)
  z2 = function(y2)
  z3 = function(y3)
  z4 = function(y4)
  
  d1 = ((z1-0)*z1*(1-z1)*1) + ((z2-1)*z2*(1-z2)*1) + ((z3-1)*z3*(1-z3)*1) + ((z4-1)*z4*(1-z4)*1) 
  d2 = ((z1-0)*z1*(1-z1)*0) + ((z2-1)*z2*(1-z2)*0) + ((z3-1)*z3*(1-z3)*1) + ((z4-1)*z4*(1-z4)*1)
  d3 = ((z1-0)*z1*(1-z1)*0) + ((z2-1)*z2*(1-z2)*1) + ((z3-1)*z3*(1-z3)*0) + ((z4-1)*z4*(1-z4)*1) 
  
  w0 -= (0.8*d1)
  w1 -= (0.8*d2)
  w2 -= (0.8*d3)
  
  
print("Done")  
print(w0)
print(w1)
print(w2)
print(error(w0, w1, w2, testcases))
