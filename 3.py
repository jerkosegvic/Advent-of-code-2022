import sys
ulaz = sys.stdin.read()
lines = ulaz.split("\n")

def getOrd(c):
    if ord(c) < ord('a'):
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1

ans = 0 
i = 0
while i <= len(lines) - 2:
    prva = set(lines[i])
    druga = set(lines[i + 1])
    treca = set(lines[i + 2])
    rez = prva.intersection(druga.intersection(treca))
    ans += getOrd(rez.pop())
    i += 3
        
print(ans)        
