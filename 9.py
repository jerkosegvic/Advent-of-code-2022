import sys

ulaz = sys.stdin.read()
lines = ulaz.split("\n")

posjecena = set( [(0,0)] )
pos2 = []
h = [0,0]
t = [0,0]

lines.pop()
naredbe = []
for line in lines:
    p = line.split(" ")
    for i in range(int(p[1])):
        naredbe.append(p[0])
#print(naredbe)
uze = [[0,0] for i in range(10)]


for naredba in naredbe:
    
    if naredba == 'R':
        uze[0][1] += 1
    elif naredba == 'L':
        uze[0][1] -= 1
    elif naredba == 'U':
        uze[0][0] += 1
    elif naredba == 'D':
        uze[0][0] -= 1
    for i in range(1,10):
        h = uze[i - 1]
        t = uze[i]
        if h[1] - t[1] == 2:    
            t[1] += 1
            if h[0] > t[0]:
                t[0] += 1
            elif h[0] < t[0]:
                t[0] -= 1 
        elif t[1] - h[1] == 2:    
            t[1] -= 1
            if h[0] > t[0]:
                t[0] += 1
            elif h[0] < t[0]:
                t[0] -= 1 
        elif h[0] - t[0] == 2:    
            t[0] += 1
            if h[1] > t[1]:
                t[1] += 1
            elif h[1] < t[1]:
                t[1] -= 1 
        elif t[0] - h[0] == 2:    
            t[0] -= 1
            if h[1] > t[1]:
                t[1] += 1
            elif h[1] < t[1]:
                t[1] -= 1 

    posjecena.add( (uze[9][0] , uze[9][1]))    

#print(pos2)
#print(posjecena)
print( len(posjecena) )
