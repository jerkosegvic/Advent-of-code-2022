import sys
ulaz = sys.stdin.read()
lines = ulaz.split("\n")
lines.pop()
tablica = []


for i in range(len(lines)):
    tablica.append([])
    for j in range(len(lines[i])):
        if i == 0 or i == len(lines) - 1 or j == 0 or j == len(lines[i]) - 1:
            tablica[i].append(True)     
        else:
            tablica[i].append(False)

def provjeri(x, y):
    val = int(lines[x][y])
    
    a1 = 0
    for i in range(len(lines)):
        if i <= x:
            continue
        tr = int(lines[i][y])
        a1 +=1
        if tr >= val:
            break
        

    a2 = 0    
    for i in reversed(range(x)):
        tr = int(lines[i][y])
        a2 +=1
        if tr >= val:
            break
        
        
    a3 = 0
    for i in reversed(range(y)):
        tr = int(lines[x][i])
        a3 +=1
        if tr >= val:
            break
        
        
    a4 = 0
    for i in range(len(lines[x])):
        if i <= y:
            continue
        tr = int(lines[x][i])
        a4 +=1
        if tr >= val:
            break
        
    
    return a1*a2*a3*a4
    
    
sol = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        tl = provjeri(i,j)
        if tl > sol:
            sol = tl
        print(tl, end = ' ')
    print('')
print(sol)
