# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 08:53:24 2021

@author: User
"""
from collections import Counter

with open('6data.txt', 'r') as file_in:
    l = file_in.read()


l_age = Counter({'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0})
l_age.update(l)

for i in range(256):
    temp_age = Counter()
    temp_age.update({'0': l_age['1'], 
                      '1': l_age['2'], 
                      '2': l_age['3'], 
                      '3': l_age['4'], 
                      '4': l_age['5'],
                      '5': l_age['6'],
                      '6': (l_age['7'] + l_age['0']),
                      '7': l_age['8']})
    if l_age['0']:
        temp_age.update({'8':l_age['0']})
    l_age = temp_age

print(sum(l_age.values()))





