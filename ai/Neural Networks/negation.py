def function(y):
  z = (1+(math.e**-y))**-1
  return z

def error(w0, w1, testcases):
  #y1 = w0 + (w1*0)
  #y2 = w0 + (w1*1)
  #return 0.5*(((1 - function(y1))**2 ) + ((0 - function(y2))**2))
  error = 0
  for case in testcases:
    y = w0 + (w1*case)
    error = error + ((testcases[case] - function(y))**2)
  return 0.5*error 

import math

w0 = 0
w1 = 0

x1 = 0
x2 = 1

testcases = {0:1,1:0}

dw = .1

'''
while(error(w0,w1, testcases) > 10**-6):
  print(w0)
  print(w1)
  errorr = error(w0, w1, testcases)
  error0 = error(w0 + dw, w1, testcases)
  error1 = error(w0, w1 + dw, testcases)
  
  d1 = (error0 - errorr)/dw
  d2 = (error1 - errorr)/dw
  
  w0 -= (0.8*d1)
  w1 -= (0.8*d2)
''' 


while(error(w0, w1,testcases) > 10**-6):
  y1 = w0 + (w1*0)
  y2 = w0 + (w1*1)
  
  z1 = function(y1)
  z2 = function(y2)
  
  dw0 = ((z1-1)*(z1)*(1-z1))+((z2-0)*(z2)*(1-z2))
  dw1 = ((z1-1)*(z1)*(1-z1)*x1)+((z2-0)*(z2)*(1-z2)*x2)
  
  w0 -= dw0
  w1 -= dw1

  
print(w0)
print(w1)
print(error(w0, w1, testcases))

    
  
    