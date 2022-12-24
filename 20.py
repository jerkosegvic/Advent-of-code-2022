import sys
from itertools import cycle
from copy import deepcopy
import copy

class element:
    elements = []
    def __init__(self, value, index):
        self.value = value
        self.index = index
        element.elements.append(self)

    def get(index):
        for element in element.elements:
            if element.index == index:
                return element
        return None

    def get_index(self, lista):
        for i in range(len(lista)):
            if lista[i] == self:
                return i
        return None

    def __eq__(self, other):
        return self.value == other.value and self.index == other.index

    def find_by_value( value, lista):
        for element in lista:
            if element.value == value:
                return element
        return None

    def __str__(self):
        return  self.value 
lnn = 0
#function which moves item i n times in list to the right and if it reaches the end it goes to the beginning
def move_forward(lista, n, i):
    ind = i.get_index(lista)
    nind = (ind + n) % (lnn - 1)
    lista.pop(ind)
    if n == -ind:
        lista.append(i)
    else:
        lista.insert(nind, i)
    return lista




def print_list(lista):
    for i in lista:
        print(i, end = " ")
    print()        

ulaz = sys.stdin.read()
lines = ulaz.split("\n")
#lines.pop()
lnn = len(lines)
broj = -1
def f(x):
    global broj
    broj = broj + 1
    return element( int(x) * 811589153, broj)

#print(lines)
#print(broj)

lines2 = list( map ( f , lines) )
lines3 = copy.deepcopy(lines2)
for _ in range(10):
    for i in lines2:
        lines3 = move_forward(lines3, int(i.value), i)
    

"""
for i in range(lnn):
    for j in range(lnn):
        if lines3[j].index == i:
            num = lines3[j]
            lines3.pop(j)
            if int(num.value) == -j:
                lines3.append(num)
            else:
                lines3.insert((int(num.value) + j) % (lnn - 1), num)
            break
"""


i0 = (element.find_by_value(0, lines3)).get_index(lines3)
#print(lines3[i0].value)
i1 = (1000 % lnn + i0) % lnn
i2 = (2000 % lnn + i0) % lnn
i3 = (3000 % lnn + i0) % lnn

print(int(lines3[i1].value) + int(lines3[i2].value) + int(lines3[i3].value))
