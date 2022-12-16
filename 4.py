import sys
ulaz = sys.stdin.read()
lines = ulaz.split("\n")
 
ans = 0
for line in lines:
    if line == "":
        break
    pom = line.split(",")
    pom1 = pom[0].split("-")
    pom2 = pom[1].split("-")
    if set(range ( int(pom1[0]) , int(pom1[1]) + 1 ) ).intersection( set( range ( int(pom2[0]) , int(pom2[1]) + 1 ) ) ):
        ans += 1
        
print(ans)  
