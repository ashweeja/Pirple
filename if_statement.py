# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:41:15 2021

Script to demosnstrate the use of "if" statement

@author: hl.ashweeja
"""

def compare(var1, var2, var3):
    """Compares 3 parameters for equality."""
    if str(var1) == str(var2) or str(var2) == str(var3) or str(var1) == str(var3):
        print("2 or more parameters are equal")
        return True
    else:
        print("No parameters are equal")
        return False
    
print(compare(1,2,3))
print(compare(2,2,3))
print(compare(3,3,3))

print(compare(3.5,"3.5",3))
print(compare(2,"2",3))
print(compare(3,'3',"3"))