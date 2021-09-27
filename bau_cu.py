s = str(input()).split(' ')
n = int(s[0])
m = int(s[1])
a = list(map(int, input().strip().split()))[:n]
a.sort()
b = []
mx = 0
for i in range(len(a)):
    b.append(a.count(a[i]))
    mx = max(a.count(a[i]), mx)
b.sort()
mx2 = 0
flat = True
for i in range(len(b)-1, -1, -1):
    if(b[i] < mx):
        flat = False
        mx2 = b[i]
        break
for i in range(len(a)):
    if(a.count(a[i]) == mx2):
        print(a[i])
        break
if(flat):
    print('NONE')
