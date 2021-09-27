s = str(input())
dem1 = 0
dem2 = 0
for i in range(len(s)):
    if s[i] >= 'a' and s[i] <= 'z':
        dem1 += 1
    elif s[i] >= 'A' and s[i] <= 'Z':
        dem2 += 1
if dem1 >= dem2:
    print(s.lower())
else :
    print(s.upper())
