# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:22:07 2021

@author: User
"""

import numpy as np

with open('testdata.txt', 'r') as file_in:
    numbers, *boards = file_in
    
boards = np.loadtxt(boards, int).reshape(-1,5,5) #-1 is z, 5 is x, 5 is y

for n in map(int, numbers.split(',')): #splits then turns everything into integers
    boards = np.where(boards == n, -1, boards)  ## simpler version b[b == n] = -1
    marked = np.where(boards == -1, True, False) # simpler version marked = (boards == -1)
    win = (marked.all(1) | marked.all(2)).any(1) #finds true on rows, uses that as input for finding columns
    if win.any():
        print((boards * ~marked)[win].sum() * n) #marks negative -1 as false so it wont be summed. Uses win as index by removing falses
        boards = boards[~win]
   
        

    
    



