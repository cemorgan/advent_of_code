with open('testdata.txt', 'r') as file_in:
    numbers, *boards = file_in.read().splitlines()


numbers = [int(i) for i in numbers.split(',')]
boards = [i.replace('  ',' ').strip() for i in boards if i]

score = 0
def check_won(card):
    won = 0
    for c in range(len(card)):
        if sum(card[c]) == -5:
            won = 1
        else:
            pass
    for i in range(5):
        if card[0][i] + card[1][i] + card[2][i] + card[3][i] + card[4][i] == -5:
            won = 1
        else:
            pass
    return won

def score(card, num):
    score = 0
    for i in range(len(card)):
        for x in range(len(card[i])):
            if card[i][x] == -1:
                card[i][x] = 0
    for a in range(len(card)):
        score += sum(card[a])
    answer = score * num
    
    return answer
        

for i in (range(len(boards))):
    boards2 = [x.split(' ') for x in boards]

boards = boards2
del boards2

for i in (range(len(boards))):
    for x in range(len(boards[i])):
        boards[i] = [int(s) for s in boards[i]]

boards2 = []
for i in (range(len(boards[::5]))):
    boards2.append(boards[i*5:i*5+5])
    
boards = boards2
del boards2

answer = 0
b_list = []
for i in range(len(numbers)):
    answer = 0
    boards2 = [boards[x] for x in range(len(boards)) if x not in b_list]
    boards = boards2
    del boards2
    if len(boards) == 0:
        break
    for b in range(len(boards)):
        for c in range(len(boards[b])):
            for n in range(len(boards[b][c])):
                if boards[b][c][n] == numbers[i]:
                    boards[b][c][n] = -1
                    verdict = check_won(boards[b])
                    if verdict == 1:
                        answer = score(boards[b], numbers[i])
                        if answer:
                            print(boards)
                            break
                    else:
                        pass
                elif answer:
                    break
                else:
                    pass
            if answer:
                break
        if answer:
            b_list.append(b)
            print(b_list)
            break
        
print(answer)


            
        

