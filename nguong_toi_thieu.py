s = str(input())
k = int(input())
a = []
for i in range(0, len(s)-1, 2):
    sum = s[i]+s[i+1]
    a.append(sum)
a.sort()
b = []
for i in a:
    if i not in b:
        b.append(i)
flat = True
for i in b:
    if(a.count(i) >= k):
        print(i, a.count(i))
        flat = False
if(flat):
    print('NOT FOUND')