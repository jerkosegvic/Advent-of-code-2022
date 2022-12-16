s = input()

ln = len(s)
i = 0

while i < ln:
    st = set()
    for l in range(14):
        st.add(s[i+l])
    if len(st) == 14:
        break
    i +=1        
print(i + 14)    
