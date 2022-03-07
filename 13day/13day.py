# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 20:41:52 2021

@author: User
"""

from collections import Counter

import numpy as np

def folding(d, n, a):
    k = [x for x in d.keys()]
    if a == 1:    
        for i in range(len(k)):
            if k[i][a] > n:
                new = (n - (k[i][a] - n))
                new = tuple([k[i][a - 1], new])
                d.subtract({k[i]: 100})
                d.update({new: 1})
    else:
        for i in range(len(k)):
            if k[i][a] > n:
                new = (n - (k[i][a] - n))
                new = tuple([new, k[i][a - 1]])
                d.subtract({k[i]: 100})
                d.update({new: 1})
    return d
            


with open('13data.txt') as file_in:
    coord, *fold = file_in.read().split('\n\n')
    
coord = [x.split(',') for x in coord.split('\n')]
coord = [[int(x) for x in y] for y in coord]
coord = [tuple(x) for x in coord]

fold = [x.strip('fold along ') for x in fold[0].split('\n')]

coord = Counter(coord)

for i in range(len(fold)):
    if 'y' in fold[i]:
        y = int(fold[i][2:])
        coord = folding(coord, y, 1)
        
    else:
        x = int(fold[i][2:])
        coord = folding(coord, x, 0)
        
    coord = {key:val for key, val in coord.items() if val > 0}
    coord = Counter(coord)
    
keys = [x for x in coord.keys()]
x_max = max(x for x,y in coord.keys()) + 1
y_max = max(y for x,y in coord.keys()) + 1

arr = np.full([y_max, x_max], '.')

for i in range(len(arr)):
    for a in range(len(keys)):
        if keys[a][-1] == i:
            arr[i][(keys[a][0])] = '#'
    

# if 'y' in fold[0]:
#     y = int(fold[0][2:])
#     coord = folding(coord, y, 1)
        
# else:
#     x = int(fold[0][2:])
#     coord = folding(coord, x, 0)
        
# coord = {key:val for key, val in coord.items() if val > 0}
# coord = Counter(coord)
    
    
