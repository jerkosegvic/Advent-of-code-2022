import copy
class bartol:
    majmuni = []
    def __init__(self, key, items, operation, condition, op_true, op_false):
        self.key = key
        self.items = items
        self.operation = operation
        self.condition = condition
        self.op_true = op_true
        self.op_false = op_false
        self.counter = 0
        bartol.majmuni.append(self)
             
    def execute_all(self):
        for i in self.items:
            self.execute(i)
        self.counter += len(self.items)
        self.items = []
    
    def get(key):
        try:
            majmun =  list ( filter( (lambda x: x.key == key) , bartol.majmuni) ) 
            return majmun[0]
        except:
            print("nekaj se zjebalo")
            
    def send(key, val):
        majmun = bartol.get(key)
        #print("TRENUTNI MAJMUN JE " + str(majmun))
        val = val % 9699690
        majmun.items.append(val)
    
    def __str__(self):
        return "Majmun s kljucem " + str(self.key) + " ima iteme " + str(self.items) + " i counter mu je " + str(self.counter) +  "\n"
    
    def execute(self, item):
        aftop = self.operation(item)
        #aftop = aftop // 3
        if self.condition(aftop):
            bartol.send(self.op_true, aftop)
        else:
            bartol.send(self.op_false, aftop)
    
    def __gt__(self, other):
        return self.counter < other.counter
    
"""   
import sys
majmun0 = bartol( 0, [79, 98], (lambda x: x * 19), (lambda x: x % 23 == 0), 2, 3)
majmun1 = bartol( 1, [54, 65, 75, 74], (lambda x: x + 6), (lambda x: x % 19 == 0), 2, 0)
majmun2 = bartol( 2, [79, 60, 97], (lambda x: x * x), (lambda x: x % 13 == 0), 1, 3)
majmun3 = bartol( 3, [74], (lambda x: x + 3), (lambda x: x % 17 == 0), 0, 1)
"""

majmun0 = bartol( 0, [50, 70, 89, 75, 66, 66], (lambda x: x * 5), (lambda x: x % 2 == 0), 2, 1)
majmun1 = bartol( 1, [85], (lambda x: x * x), (lambda x: x % 7 == 0), 3, 6)
majmun2 = bartol( 2, [66, 51, 71, 76, 58, 55, 58, 60], (lambda x: x + 1), (lambda x: x % 13 == 0), 1, 3)
majmun3 = bartol( 3, [79, 52, 55, 51], (lambda x: x + 6), (lambda x: x % 3 == 0), 6, 4)
majmun4 = bartol( 4, [69, 92], (lambda x: x * 17), (lambda x: x % 19 == 0), 7, 5)
majmun5 = bartol( 5, [71, 76, 73, 98, 67, 79, 99], (lambda x: x + 8), (lambda x: x % 5 == 0), 0, 2)
majmun6 = bartol( 6, [82, 76, 69, 69, 57], (lambda x: x + 7), (lambda x: x % 11 == 0), 7, 4)
majmun7 = bartol( 7, [65, 79, 86], (lambda x: x + 5), (lambda x: x % 17 == 0), 5, 0)


maj = bartol.get(1)

print("NA POCETKU JE OVAKO : ")
for majmun in bartol.majmuni:
        print(str(majmun))   


for i in range(10000):
    for majmun in bartol.majmuni:
        majmun.execute_all()
    if(i % 1000 == 0):
        print("EPOHA" + str(i) + " :\n------------------------------------------------------------")
        for majmun in bartol.majmuni:
            print(str(majmun))   

bartol.majmuni.sort()
#for majmun in bartol.majmuni:
#    print(str(majmun.key) + " -> " + str(majmun.items) + "\n")

sol = bartol.majmuni[0].counter * bartol.majmuni[1].counter

print(sol) 
