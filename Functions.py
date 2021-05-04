# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:35:26 2021

@author: hl.ashweeja
"""

#Declaring the global variables
SongName = "abcd"
SingerName = "def"
DurationInMins = 4.35
SizeInMb = 5.2
SongType = "Jazz"
AlbumYear = 2021
SongRating = 9.5
Language = "English"

def language():
    return Language

def songtype():
    return SongType

def albumyear():
    return AlbumYear

def isSongLengthy():
    """  If song duration is more than 4 mins, its lenthy.
    
    @returns:
        True: If duration is more than 4 mins.
        False: If duration is less than 4 mins.
    """
    if DurationInMins > 4:
        return True
    else:
        return False

print(language())
print(songtype())
print(albumyear())
print(isSongLengthy())