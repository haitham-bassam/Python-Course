# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:16:08 2018

@author: Haitham
"""
# all the letter must be in small case 
x=input("if you want to convarte from Celsuis to Fahrenheit Type 'c' otherwise type 'f' : ")
y=float(input("Enter the Temperature: "))
if x == "c" :
    y=1.8*y+32
    
if x == "f" :
    y=(y-32)/1.8    
    
print(y)    