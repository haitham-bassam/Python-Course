# -*- coding: utf-8 -*-
"""
Spyder Editor
import math

This is a temporary script file.
"""
import math
x=int(input("Enter your number: "))
if x<-100 :
       x=-x
    
elif -100 <= x <= -25:
    x=x**4
elif -25 < x <= 0 :
    x=3*x**2-1
elif 0 < x <= 100 :
    x=math.pi/2*x + 3**x
    
else :
    x=x
    
print("%.1f" % float(x))    
    
    
    
#  answer for 1.D : Float is the answer because division may be exist and the result from the division is float
       