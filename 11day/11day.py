# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 20:53:01 2021

@author: User
"""

import numpy as np                        
from scipy.signal import convolve as cv

def flash_growth(board, convolve, new, answer):
    h_e = board > 9
    f = cv(new, convolve, mode = 'same')
    board = board + f
    nh_e = board > 9
    new = np.logical_xor(h_e, nh_e)
    answer += np.count_nonzero(new)
    
    return board, new, answer

with open('11data.txt') as file_in:
    board = file_in.read().splitlines()
    board = [list(x) for x in board]
    file_in.close()
    
board = np.array(board, dtype=int)
convolve = np.ones((3,3))

answer = 0

for i in range(1000):
    board = np.add(board, 1)
    new = board > 9
    answer += np.count_nonzero(new)
    board, new, answer = flash_growth(board, convolve, new, answer)
    while new.any():
        board, new, answer = flash_growth(board, convolve, new, answer)
    board = np.where(board > 9, 0, board)
    if np.all(board == 0):
        break
        
print(i + 1)
        
    
    
