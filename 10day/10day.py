# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:52:24 2021

@author: User
"""


def complete(_stack, _cc, points):
    _score = 0
    for i in range(len(_stack) - 1, -1, -1):
        _score = _score * 5 + points[_cc.index(_stack[i])]
    
    return _score
        

with open('10data.txt', 'r') as file_in:
    data = file_in.read().splitlines()

oc = ['(', '[', '{', '<']
cc = [')', ']', '}', '>']
score = [3, 57, 1197, 25137]
c_score = [1, 2, 3, 4]
stack = []
ill = []
inc = []
answer = 0
answer2 = []


for i in data:
    stack = []
    for x in range(len(i)):
        if i[x] in oc:
            stack.append(cc[oc.index(i[x])])
            if x == len(i) - 1:
                answer2.append(complete(stack, cc, c_score))
        elif i[x] == stack[-1]:
            stack.pop()
            if x == len(i) - 1:
                answer2.append(complete(stack, cc, c_score))
        else:
            ill.append(i[x])
            break
            
for i in range(len(ill)):
    answer += score[cc.index(ill[i])]

answer2 = sorted(answer2)
final = answer2[int((len(answer2) - 1) / 2)]

#print(answer)
print(final)