import sys

ulaz = sys.stdin.read()
lines = ulaz.split("\n")
lines.pop()


sol = 0
tmp = []

def comp_list(x, y):
    #print("x je " + str(x) + ", a y je " + str(y) + "\n")
    if type(x) == int:
        x = [x]
    else:
        x = list(x)        
    if type(y) == int:
        y = [y]
    else:
        y = list(y)
    #print("x je " + str(x) + ", a y je " + str(y) + "\n")        
    gr = min(len(x), len(y))
    #print(len(x) == len(y) == 1)
    #print( str (type(x)) +  str( type(y) ))
    if len(x) != 0 and len(y) == 0:
        return "return False"
    if len(y) != 0 and len(x) == 0:
        return "return True"
    if len(x) == 0 and len(y) == 0:
        return "continue"
    if len(x) == len(y) == 1 and not (type(x[0]) == list or type(y[0]) == list ):
        if x[0] < y[0]:
            return "return True"
        elif x[0] == y[0]:
            return "continue"
        else:
            return "return False"
    x = list(x)
    y = list(y)
    #print("RETARDIRAN SAM")
    i = 0
    while i < gr:
        xx = x[i]
        yy = y[i]
        rv = comp_list(xx,yy)
        #print( "xx je " + str(xx) + " yy je " + str(yy) + ", rv je " + str(rv) + "\n")
        if rv != "continue":
            return rv
        i+=1 
    if len(x) < len(y):
        return "return True"       
    if len(x) == len(y):
        return "continue"       
    return "return False"
     
def provjeri (x, y):
    #xlist = eval(x)
    #ylist = eval(y)
    
    xlist = x
    ylist = y
    
    rv = comp_list(xlist, ylist)
    if rv == "continue":
        return True
    
    elif rv == "return True":
        return True

    return False
    
#print(lines)        
niz = []
niz.append([[2]])
niz.append([[6]])
tm = 1    
for line in lines:
    if line == '':
        continue
    p = eval(line)
    niz.append(p)

import copy
s_niz = copy.deepcopy(niz)
for i in range(len(niz)):
    for j in range(len(niz)):
        li = copy.deepcopy(s_niz[i])
        ji = copy.deepcopy(s_niz[j])
        if provjeri(li, ji):
            s_niz[i] = ji
            s_niz[j] = li            
i = 1 
"""
print("nesortirani niz:")
for n in niz:
    print(str(i) + " --> " + str(n) + "\n")
    i +=1

i = 0
print("sortirani niz:")
for n in s_niz:
    print(str(i) + " --> " + str(n) + "\n")
    i +=1
"""
print((1 + s_niz.index(niz[0])) * (1 + s_niz.index(niz[1])))
