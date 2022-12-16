import sys
ulaz = sys.stdin.read()
lines = ulaz.split("\n")

master = 0
polje = []

for i in range (100):
    polje.append([])

for line in lines:
    if line[1].isnumeric():
        break
    master+=1



for line in lines:
    i = 0
    while i < len(line):
        tren = line[i]
        if tren == '[':
            ind = int ( lines[master][i + 1]) - 1
            polje[ind].insert(0 ,line[i + 1])
        i+=1
    if lines.index(line) == master:
        break

naredbe = []
i = master + 2       

def pomakni(koliko, s , na):
    uzorak = list ( polje[s][-koliko:]  ) 
    polje[s] = polje[s][:len(polje[s]) - koliko]
    polje[na] = polje[na] + uzorak
    

while i < len(lines):
    line = lines[i]
    if line == "":
        break
    ls = line.split(" ")
    pomakni( int( ls[1] ) , int( ls[3] ) - 1, int( ls[5] ) - 1 )
    i += 1
    
for i in polje:
    if len(i) == 0:
        break
    print(i.pop() , end = '')
print('')        
