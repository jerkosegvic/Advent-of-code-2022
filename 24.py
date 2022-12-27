import sys

ulaz = sys.stdin.read()
lines = ulaz.split("\n")
gr = len(lines[0])
mod1 = gr - 2
mod2 = len(lines) - 2
mod3 = 700
mapa1 = []
mapa2 = []
for i in range(gr):
    mapa1.append([])
    mapa2.append([])
    for j in range(gr):
        mapa1[i].append(set())
        mapa2[i].append(set())
print("MOD1 je ", mod1)
print("MOD2 je ", mod2)
def aux(x):
    if x == '#':
        return False
    else:
        return True
ii = 0

lines2 = lines[1:-1]
#print(lines2)
for line in lines2:
    lnn = list( filter( aux ,line) )
    #print(lnn)
    ind = 0
    for l in lnn:
        if l == '<':
            for i in range(mod1):
                if ind <= i:
                    mapa1[ii][i].add((mod1 - abs(ind - i)) % mod1)
                else:
                    mapa1[ii][i].add(abs(ind - i))
        elif l == '>':
            for i in range(mod1):
                if ind <= i:
                    mapa1[ii][i].add(abs(ind - i))
                else:
                    mapa1[ii][i].add((mod1 - abs(ind - i)) % mod1)
        elif l == '^':
            for i in range(mod2):
                if ii <= i:
                    mapa2[i][ind].add((mod2 - abs(ii - i)) % mod2)
                else:
                    mapa2[i][ind].add(abs(ii - i))

        elif l == 'v':
            for i in range(mod2):
                if ii <= i:
                    mapa2[i][ind].add(abs(ii - i))
                else:
                    mapa2[i][ind].add( (mod2 - abs(ii - i)) % mod2)
        ind += 1   
    ii += 1
"""
for m in mapa:
    for mm in m:
        print(mm, end=" ")
    print()
"""


def ok(x, y, t, mem, sx, sy, cx, cy):
    tp = (x, y, t % mod3)
    if tp in mem:
        return False
    if x == sx and y == sy:
        return True
    if x == cx and y == cy:
        return True
    if x < 0 or x >= mod2 or y < 0 or y >= mod1:
        return False
    if t % mod1 in mapa1[x][y] or t % mod2 in mapa2[x][y]:
        return False
    return True

def dp (sx, sy, st, cx, cy):
    q = []
    mem = set()
    q.append((sx, sy, st))
    while not len(q) == 0:
        tren = q.pop(0)
        x = tren[0]
        y = tren[1]
        t = tren[2]
        if x == cx and y == cy:
            return t
            break

        lst = [(0,0), (0,1), (0,-1), (1,0), (-1,0)]
        for l in lst:
            nx = x + l[0]
            ny = y + l[1]
            if ok(nx, ny, t + 1, mem, sx, sy, cx, cy):
                q.append((nx, ny, t + 1))
                mem.add((nx, ny, (t + 1) % mod3))

t1 = dp(-1, 0, 0, mod2, mod1 - 1)
t2 = dp(mod2, mod1 - 1, t1, -1, 0)
t3 = dp(-1, 0, t2, mod2, mod1 - 1)
print(t3)