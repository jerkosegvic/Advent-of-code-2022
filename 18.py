import sys
from copy import deepcopy
import copy
import math

ulaz = sys.stdin.read()
lines = ulaz.split("\n")
sol = 6 * len(lines)

ln = []
for line in lines:
    if line == "$":
        break
    xs = list(map( (lambda x: int(x)) , line.split(',')))
    ln.append(xs)
polje = []

sol = 6 * len(ln)
#print(ln)
for i in ln:
    for j in ln:
        if i != j:
            if i[0] == j[0] and i[1] == j[1] and abs(i[2] - j[2]) == 1:
                sol -= 1
            if i[2] == j[2] and i[1] == j[1] and abs(i[0] - j[0]) == 1:
                sol -= 1
            if i[0] == j[0] and i[2] == j[2] and abs(i[1] - j[1]) == 1:
                sol -= 1

print(sol)
           
    