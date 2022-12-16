import sys
ulaz = sys.stdin.read()
lines = ulaz.split("\n")
#print(lines)
dct = {
    'A': { 'X' : 3, 'Y' : 4, 'Z' : 8},
    'B': { 'X' : 1, 'Y' : 5, 'Z' : 9},
    'C': { 'X' : 2, 'Y' : 6, 'Z' : 7}
}
ans = 0
for line in lines:
    try:
        aux = line.split(' ')
        ans += dct[ aux[0] ] [ aux[1] ]
    except:
        break

print(ans)
