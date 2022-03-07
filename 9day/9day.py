# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:57:30 2021

@author: User
"""


with open('9data.txt', 'r') as file_in:
    data = file_in.read().splitlines()
    
for i in range(len(data)):
    data[i] = [int(x) for x in list(data[i])]


for i in range(len(data)):
    data[i].insert(len(data[i]), 9)
    data[i].insert(0, 9)
    
nines = [9] * len(data[0])

data.insert(0, nines)
data.append(nines)


lowest = []

for i in range(len(data[1:-1])):
    for x in range(len(data[i][1:-1])):
        if data[i+1][x+1] < data[i][x+1]:
            if data[i+1][x+1] < data[i+2][x+1]:
                if data[i+1][x+1] < data[i+1][x]:
                    if data[i+1][x+1] < data[i+1][x+2]:
                        lowest.append(data[i+1][x+1])

                    
answer = sum([i+1 for i in lowest])