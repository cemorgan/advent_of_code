# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 00:07:55 2021

@author: User
"""

from string import ascii_uppercase as up

from collections import Counter
            
with open('14data.txt') as file_in:
    poly, *inst = file_in.read().split('\n\n')
    
inst = inst[0].splitlines()
inst = [x.split(' -> ') for x in inst]

key = [poly[x:x+2] for x in range(len(poly)-1)] #start populating pairs list
key = Counter(key)  #pairs list to dictionary
ref_key = {x[0]:0 for x in inst} #creates unpopulated ref dict will all pairs
key.update(ref_key) #merges populated pairs dict with unpopulated ref keys
t_key = Counter(ref_key) #ref key to counter

answer = {x:0 for x in up} #set up final answer dict with all uppercase letters
answer = Counter(answer)

for i in poly:
    answer.update(i) #populated final answer dict with poly
    
for x in range(40):    
    for i in range(len(inst)):
        cnt = key[inst[i][0]] #how many times pair matches
        if cnt >= 1:
            new = f'{inst[i][0][0]}{inst[i][1]}'  
            new2 = f'{inst[i][1]}{inst[i][0][1]}'
            t_key.subtract({inst[i][0]:cnt})  #removes matched pairs
            t_key.update({new:cnt, new2:cnt}) #adds two pairs with new letter
            answer.update({inst[i][1]:cnt}) #update answer with new letter
        else:
            pass
    
    key = key + t_key  #reset everything
    t_key = dict.fromkeys(t_key, 0)
    t_key = Counter(t_key)

final = {x:y for (x,y) in answer.items() if y != 0}
print(max(final.values()) - min(final.values()))

    
    



