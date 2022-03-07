# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 16:24:31 2021

@author: User
"""

import numpy as np

def s_clean(f):
    f = f.split(' | ')

    return f

def alph(f):
    e = ''.join(sorted(f))
    return e

def find_u(digit, output, number):
    for y in range(len(output)):
        if np.isin(output[y], digit):
            output[y] = number
    return output
    
def find_6(output, length, digit, answer):
    b = list(digit)
    output = output[length == 6]
    for i in range(len(output)):
        marked = np.isin(output[i], b)
        yes = marked.all()
        if yes:
            return answer

with open('testdata.txt', 'r') as file_in:
    data = file_in.read().splitlines()

s = []
o = []

for i in map(s_clean, data):
    s.append(i[0].split())
    o.append(i[1].split())

for i in range(len(s)):
    s[i] = list(map(alph, s[i]))
    o[i] = list(map(alph, o[i]))


s_arr = np.array(s, dtype=str)
o_arr = np.array(o, dtype=str) 

length_check = np.vectorize(len)
l_arr = length_check(s_arr)


_i = s_arr[l_arr == 2]
iv = s_arr[l_arr == 4]
vii = s_arr[l_arr == 3]
viii = s_arr[l_arr == 7]


for i in range(len(o_arr)):
    find_u(_i[i], o_arr[i], 1)
    find_u(iv[i], o_arr[i], 4)
    find_u(vii[i], o_arr[i], 7)
    find_u(viii[i], o_arr[i], 8)



    



    
