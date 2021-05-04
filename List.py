# -*- coding: utf-8 -*-
"""
Created on Tue May  4 09:45:30 2021

Script to demonstrate the usage of lists

@author: hl.ashweeja
"""

#Global lists
myUniqueList = []
myLeftovers = []


def addToList(value):
    """Add the values to global list if value is not present already."""
    if value in myUniqueList:
        print(value,"is already present in list")
        addToLeftover(value)
        return False

    myUniqueList.append(value)
    print(value, "added to list successfully")
    return True


def addToLeftover(value):
    """Add the values to leftovers list."""
    myLeftovers.append(value)
    return True

# Add values to list
addToList(1)
addToList(2)
addToList(3)
addToList(1)
addToList(2)
addToList(4)

#print global list
print(myUniqueList)
print(myLeftovers)