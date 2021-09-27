s = str(input())
a = []
for i in range(0, len(s)-1, 2):
    sum = s[i]+s[i+1]
    a.append(sum)
b = []
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(i, end=' ')