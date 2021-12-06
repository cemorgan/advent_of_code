with open('testdata.txt', 'r') as file_in:
    data = file_in.read().splitlines()
data = [data[x].replace(' -> ', ' ') for x in range(len(data))]
data = [data[x].split() for x in range(len(data))]
ready_data = []

for i in range(len(data)):
    ready_data.append([data[i][x].split(',') for x in range(len(data[i]))])
    
diagonals = []
for i in range(len(ready_data)):
    if ready_data[i][0][0] == ready_data[i][1][0]:
        pass
    elif ready_data[i][0][1] == ready_data[i][1][1]:
        pass
    elif (abs(int(ready_data[i][0][0]) - int(ready_data[i][1][0])) == abs(int(ready_data[i][0][1]) - int(ready_data[i][1][1]))):
        pass
    else:
        diagonals.append(i)

new_data = [data[x] for x in range(len(data)) if x not in diagonals]
grid = {}

print(diagonals)

for i in range(len(new_data)):
    if new_data[i][0] in grid.keys():
        grid[new_data[i][0]] = grid[new_data[i][0]] + 1
        if new_data[i][1] in grid.keys():
            grid[new_data[i][1]] = grid[new_data[i][1]] + 1
        else:
            grid.update({new_data[i][1]: 1})
    elif new_data[i][1] in grid.keys():
        grid[new_data[i][1]] = grid[new_data[i][1]] + 1
        if new_data[i][0] in grid.keys():
            grid[new_data[i][0]] = grid[new_data[i][0]] + 1
        else:
            grid.update({new_data[i][0]: 1})
    else:
        grid.update({new_data[i][0]: 1})
        grid.update({new_data[i][1]: 1})

del data
del new_data


def find_coord(ye_old_map, coords):
    for i in range(len(ye_old_map)):
        if ye_old_map[i][0][0] == ye_old_map[i][1][0]:
            if int(ye_old_map[i][0][1]) > int(ye_old_map[i][1][1]):
                for x in range(int(ye_old_map[i][0][1]) - int(ye_old_map[i][1][1]) - 1):
                    temp = f'{ye_old_map[i][1][0]},{int(ye_old_map[i][1][1]) + x + 1}'
                    if temp in coords.keys():
                        coords[temp] = coords[temp] + 1
                    else:
                        coords.update({temp: 1})
            else:
                for x in range(int(ye_old_map[i][1][1]) - int(ye_old_map[i][0][1]) - 1):
                    temp = f'{ye_old_map[i][0][0]},{int(ye_old_map[i][0][1]) + x + 1}'
                    if temp in coords.keys():
                        coords[temp] = coords[temp] + 1
                    else:
                        coords.update({temp: 1})
        elif ye_old_map[i][0][1] == ye_old_map[i][1][1]:
            if int(ye_old_map[i][0][0]) > int(ye_old_map[i][1][0]):
                for x in range(int(ye_old_map[i][0][0]) - int(ye_old_map[i][1][0]) - 1):
                    temp = f'{int(ye_old_map[i][1][0]) + x + 1},{ye_old_map[i][1][1]}'
                    if temp in coords.keys():
                        coords[temp] = coords[temp] + 1
                    else:
                        coords.update({temp: 1})
            else:
                for x in range(int(ye_old_map[i][1][0]) - int(ye_old_map[i][0][0]) - 1):
                    temp = f'{int(ye_old_map[i][0][0]) + x + 1},{ye_old_map[i][0][1]}'
                    if temp in coords.keys():
                        coords[temp] = coords[temp] + 1
                    else:
                        coords.update({temp: 1})
        elif abs(int(ye_old_map[i][0][0]) - int(ye_old_map[i][1][0])) == abs(int(ready_data[i][0][1]) - int(ready_data[i][1][1])):
            if int(ye_old_map[i][0][0]) < int(ye_old_map[i][1][0]):
                 if int(ye_old_map[i][0][1]) < int(ye_old_map[i][1][1]):    
                     for x in range(abs(int(ye_old_map[i][0][0]) - int(ye_old_map[i][1][0])) - 1):
                         temp = f'{int(ye_old_map[i][0][0]) + x + 1},{int(ye_old_map[i][0][1]) + x + 1}'
                         if temp in coords.keys():
                             coords[temp] = coords[temp] + 1
                         else:
                             coords.update({temp: 1})
                 else:
                     for x in range(abs(int(ye_old_map[i][0][0]) - int(ye_old_map[i][1][0])) - 1):
                         temp = f'{int(ye_old_map[i][0][0]) + x + 1},{int(ye_old_map[i][0][1]) - x - 1}'
                         if temp in coords.keys():
                             coords[temp] = coords[temp] + 1
                         else:
                             coords.update({temp: 1})
                         
            else:
                 if int(ye_old_map[i][0][1]) < int(ye_old_map[i][1][1]):    
                     for x in range(abs(int(ye_old_map[i][0][0]) - int(ye_old_map[i][1][0])) - 1):
                         temp = f'{int(ye_old_map[i][0][0]) - x + 1},{int(ye_old_map[i][0][1]) + x + 1}'
                         if temp in coords.keys():
                             coords[temp] = coords[temp] + 1
                         else:
                             coords.update({temp: 1})
                 else:
                     for x in range(abs(int(ye_old_map[i][0][0]) - int(ye_old_map[i][1][0])) - 1):
                         temp = f'{int(ye_old_map[i][0][0]) - x + 1},{int(ye_old_map[i][0][1]) - x - 1}'
                         if temp in coords.keys():
                             coords[temp] = coords[temp] + 1
                         else:
                             coords.update({temp: 1})
        else:
            pass

    return coords

def dict_pop(dic, n):
    if dic[n] == 1:
        dic.pop(n)
    return dic

abba = find_coord(ready_data, grid)
answer = 0
for i in abba:
    if abba[i] != 1:
        answer += 1
    else:
        pass
print(answer)
print(abba)
