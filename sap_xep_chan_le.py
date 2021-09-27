n = int(input())
flat = False
a = []

while 1:
    s = input().split()
    for i in range(len(s)):
        a.append(int(s[i]))
        if(len(a) == n):
            flat = True
            break
    if(flat):
        break
    
b = []
c = []
for i in range(n):
    if(a[i] % 2 == 0):
        b.append(a[i])
    else:
        c.append(a[i])
b.sort()
c.sort(reverse=True)
x = 0
y = 0
for i in range(n):
    if(a[i] % 2 == 0):
        print(b[x], end=' ')
        x+=1
    else:
        print(c[y], end=' ')
        y+=1