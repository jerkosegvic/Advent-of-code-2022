import sys

ulaz = sys.stdin.read()
lines = ulaz.split("\n")


lista = []
acc = 0
for line in lines:
    if line == "":
        lista.append(acc)
        acc = 0
    else:
        acc += int(line)

ans = 0
l = sorted(lista)
ans += l.pop()
ans += l.pop()
ans += l.pop()
print(ans)   
