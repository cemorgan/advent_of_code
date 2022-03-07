# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 12:06:08 2021

@author: User
"""

import numpy as np

def s_clean(f):
    f = f.split(' | ')

    return f


with open('testdata.txt', 'r') as file_in:
    data = file_in.read().splitlines()

s = []
o = []

for i in map(s_clean, data):
    s.append(i[0].split())
    o.append(i[1].split())


s_arr = np.array(s, dtype=str)
o_arr = np.array(o, dtype=str)


v = [2,3,4,7] 

length_check = np.vectorize(len)
length = length_check(o_arr)

marked = np.isin(length, v)
print(np.count_nonzero(marked))
        

    
    
    




