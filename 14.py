import sys
import copy

ulaz = sys.stdin.read()
lines = ulaz.split("\n")
lines.pop()

#print(lines)

tablica = []
lowest_point = 0
for t in range(1500):
    tablica.append([])
    for p in range(1500):
        tablica[t].append('.')
        
lastx = 0
lasty = 0        
for line in lines:
    points = line.split('->')
    for point in points:
        cords = (point.strip()).split(',')
        y = int(cords[0])
        x = int(cords[1])
        tablica[x][y] = '#'
        #print((x,y))
        if x > lowest_point:
            lowest_point = copy.deepcopy(x)    
            
        if point == points[0]:
            lastx = x
            lasty = y
            continue
        
        if lastx == x:
            if lasty < y:
                for i in range(lasty,y):
                    tablica[x][i] = '#'
            else:
                for i in range(y,lasty):
                    tablica[x][i] = '#'
        
        else:
            if lastx < x:
                for i in range(lastx,x):
                    tablica[i][y] = '#'
            else:
                for i in range(x,lastx):
                    tablica[i][y] = '#'                    
            
        lastx = x
        lasty = y

lowest_point += 2
for i in range(len(tablica[lowest_point])):
    tablica[lowest_point][i] = '#'

"""        
for p in tablica[:15]:
    print(p[490:505])    

print(lowest_point)
"""
sol = 0

def baci(x, y):
    while(x <= lowest_point):
        if tablica[x + 1][y] == '.':
            x += 1
        elif tablica[x + 1][y - 1] == '.':     
            y -= 1
            x += 1 
        elif tablica[x + 1][y + 1] == '.':     
            y += 1
            x += 1
        else:
            tablica[x][y] = 'o'
            break
    if x == 0 and y == 500:
        return False
    return True     
while True:
    if not baci(0,500):
        break
    sol += 1
    #print(sol)
#    if sol == 95:
#        break
"""       
for p in tablica[:15]:
    print(p[490:505])  
"""
print(sol + 1)



