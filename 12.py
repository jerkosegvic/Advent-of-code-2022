import sys
from queue import Queue

ulaz = sys.stdin.read()
lines = ulaz.split("\n")
lines.pop()

def ok(x, y):
    return x >= 0 and x < len(lines) and y >= 0 and y < len(lines[0]) 



tablica = []

posjeceni = set()
q = Queue()

for l in lines:
    for c in l:
        if c == 'S':
            x = lines.index(l)
            y = l.index(c)
        if c == 'E':
            xx = lines.index(l)
            yy = l.index(c)
print(tablica)


lines[xx] = lines[xx][:yy] + 'z' + lines[xx][yy+1:]
print(lines)

q.put((xx,yy,0))
sol = 0
while(not q.empty()):
    tren = q.get()
    tx = tren[0]
    ty = tren[1]
    val = tren[2]
    tznak = lines[tx][ty]
    if tznak == 'S':
        tznak = 'a'
    #print("evo ja sam tu")
    
    if tznak == 'a':
        print(val)
        break
    #print( "znak je " + "--" + tznak + "--")
    #print("desno: " + "--" + lines[tx + 1][ty] + "--")
    #print("dolje: " + lines[tx][ty + 1])
    if ok(tx + 1, ty) and ord(tznak) - ord(lines[tx + 1][ty])  <= 1 and ((tx + 1, ty) not in posjeceni):
        q.put((tx + 1, ty, val + 1))
        posjeceni.add((tx + 1, ty))
        
    if ok(tx - 1, ty) and ord(tznak) - ord(lines[tx - 1][ty]) <= 1 and ((tx - 1, ty) not in posjeceni):
        q.put((tx - 1, ty, val + 1))
        posjeceni.add((tx - 1, ty))
        
    if ok(tx, ty + 1) and ord(tznak) - ord(lines[tx][ty + 1]) <= 1 and ((tx, ty + 1) not in posjeceni):
        q.put((tx, ty + 1, val + 1))
        posjeceni.add((tx, ty + 1))
        
    if ok(tx, ty - 1) and ord(tznak) - ord(lines[tx][ty - 1]) <= 1 and ((tx, ty - 1) not in posjeceni):
        q.put((tx, ty - 1, val + 1))
        posjeceni.add((tx, ty - 1))
        
        
