import sys

ulaz = sys.stdin.read()
lines = ulaz.split("\n")
lines.pop()

class Valve:
    valves = []
    def __init__(self, name, value, tunnels):
        self.name = name
        self.value = value
        self.tunnels = tunnels
        Valve.valves.append(self)
    
    def get(name):
        for valve in Valve.valves:
            if valve.name == name:
                return valve
        return None

    def __str__(self):
        return "Valve: " + self.name + " value: " + str(self.value) + " tunnels: " + str(self.tunnels)

    def print_all():
        for valve in Valve.valves:
            print(valve)

    def shortest_path(start, end):
        queue = []
        queue.append(start)
        visited = []
        visited.append(start)
        distance = {}
        distance[start] = 0       
        while queue:
            current = queue.pop(0)
            #print(str(current))
            d = distance[current]            
            if current == end:
                return d
            for tunnel in current.tunnels:
                if tunnel not in visited:
                    queue.append(Valve.get(tunnel))
                    visited.append(tunnel)
                    distance[Valve.get(tunnel)] = d + 1
        return None

pocetni = lines[0].split(" ")[1]
for line in lines:
    tokens = line.split(" ")
    svalve = tokens[1]
    valu = int(tokens[4].split('=')[1].split(';')[0])
    tunnels = []
    for i in range(9, len(tokens)):
        tunnels.append(tokens[i].split(',')[0])   
    Valve(svalve, valu, tunnels)

Valve.print_all()
print(pocetni)
print(Valve.shortest_path(Valve.get(pocetni), Valve.get("HH")))

distances = {}

for i in range(0, len(Valve.valves)):
    distances[Valve.valves[i].name] = {}
    for j in range(0, len(Valve.valves)):
        distances[Valve.valves[i].name][Valve.valves[j].name] = Valve.shortest_path(Valve.valves[i], Valve.valves[j])
        #print(Valve.valves[i].name + " " + Valve.valves[j].name + " " + str(Valve.shortest_path(Valve.valves[i], Valve.valves[j])))

#print(distances)

dp = {}
for i in range(0, 30):
    dp[i] = {}
    for j in range(0, len(Valve.valves)):
        dp[i][Valve.valves[j].name] = 0

print(dp)
for i in range(1, 30):
    for j in range(0, len(Valve.valves)):
        dp[i][Valve.valves[j].name] = max(dp[i-1][Valve.valves[j].name], dp[i-1][Valve.valves[j].name] + Valve.valves[j].value)
