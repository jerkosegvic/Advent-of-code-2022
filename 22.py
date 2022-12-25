import sys
from copy import deepcopy
import copy

ulaz = sys.stdin.read()
lines = ulaz.split("\n")
gr = 208
mapa = []
mapa2 = []

for i in range(gr):
    mapa.append([])
    mapa2.append([])
    for j in range(gr):
        mapa[i].append("$")
        mapa2[i].append("$")

ind = 1        
for line in lines:
    if line == "":
        break
    else:
        for j in range(1, len(line) + 1):
            l = line[j - 1]
            if l == '.':
                mapa[ind][j] = '.'
                mapa2[ind][j] = '.'
            elif l == '#':
                mapa[ind][j] = '#'
                mapa2[ind][j] = '#'
        poc = (line.index('.'))
        kraj = (len(line) + 1)
#        print(poc, kraj)
        if mapa[ind][poc] != '#' and mapa[ind][kraj - 1] != '#':
            mapa[ind][kraj] = str(poc + 1)
        if mapa[ind][kraj - 1] == '.' and mapa[ind][poc] != '#':
            mapa[ind][poc] = str(kraj - 1)

    ind += 1
kod = lines[len(lines)-1]


for i in range(gr):
    naso = False
    kraj = -1
    for j in range(gr):
        if not naso and mapa2[j][i] == '#':
            break
        if mapa2[j][i] == '.' and not naso:
            poc = j
            naso = True
        if mapa2[j][i] == '.' and mapa2[j + 1][i] != '.' and naso:
            kraj = j
        if mapa2[j][i] == '#' and naso:
            kraj = -1
    if naso and kraj != -1:   
        mapa2[poc - 1][i] = str(kraj)
        mapa2[kraj + 1][i] = str(poc)
"""
for m in mapa:
    for mm in m:
        print(f'{mm:2}', end=" ")
    print()

print("-----------------------")
for m in mapa2:
    for mm in m:
        print(f'{mm:2}', end=" ")
    print()    
print(kod)
"""
str = ""
naredbe = []
for i in kod:
    if i == 'R':
        naredbe.append(str)
        naredbe.append(i)
        str = ""
    elif i == 'L':
        if str != '':
            naredbe.append(str)
        naredbe.append(i)
        str = ""
    else:
        str += i

#print(naredbe)

dir = 'R'
def pomak(x, y, dx, dy):
    if mapa[x + dx][y + dy] == '.':
        x += dx
        y += dy
#        print(x, y)
    elif mapa2[x + dx][y + dy] != '#' and mapa2[x + dx][y + dy] != '$' and dy == 0:
        x = int(mapa2[x + dx][y + dy])
        y += dy
#        print(x, y)
    elif mapa[x + dx][y + dy] != '#' and mapa[x + dx][y + dy] != '$' and dx == 0:
        x += dx
        y = int(mapa[x + dx][y + dy])
#        print(x, y)
    return x, y


x, y = 0, 0

br = False
for i in range(gr):
    for j in range(gr):
        if mapa[i][j] == '.':
            x, y = i, j
            br = True
            break            
    if br:
        break

#print(x, y)
for naredba in naredbe:
    if naredba == 'R':
        if dir == 'R':
            dir = 'D'
        elif dir == 'D':
            dir = 'L'
        elif dir == 'L':
            dir = 'U'
        elif dir == 'U':
            dir = 'R'
    elif naredba == 'L':
        if dir == 'R':
            dir = 'U'
        elif dir == 'D':
            dir = 'R'
        elif dir == 'L':
            dir = 'D'
        elif dir == 'U':
            dir = 'L'  
    else:
        num = int(naredba)
        if dir == 'R':
            for i in range(num):
                nx, ny = pomak(x, y, 0, 1)
                x, y = nx, ny

        elif dir == 'D':
            for i in range(num):
                nx, ny = pomak(x, y, 1, 0)
                x, y = nx, ny

        elif dir == 'L':
            for i in range(num):
                nx, ny = pomak(x, y, 0, -1)
                x, y = nx, ny

        elif dir == 'U':
            for i in range(num):
                nx, ny = pomak(x, y, -1, 0)
                x, y = nx, ny

#print(dir)
sol = 0
if dir == 'R':
    sol += 0
elif dir == 'D':
    sol += 1
elif dir == 'L':
    sol += 2
elif dir == 'U':
    sol += 3
sol += 1000*x + 4*y 
print(sol)
        