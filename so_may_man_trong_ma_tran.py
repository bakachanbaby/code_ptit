
n, m = map(int, input().split())
a = []
mx = 0
mn = 1000000
for i in range(n):
    x = list(map(int, input().split()))
    tmpmax = max(x)
    mx = max(tmpmax, mx)
    tmpmin = min(x)
    mn = min(tmpmin, mn)
    a.append(x)
flat = True

tmp = mx-mn

for i in range(n):
    for j in range(m):
        if(tmp == a[i][j]):
            flat = False
            break
    if(flat == False):
        break
if(flat):
    print('NOT FOUND')
else:
    print(tmp)
    for i in range(n):
        for j in range(m):
            if(tmp == a[i][j]):
                print("Vi tri [" + str(i) + "][" + str(j) + "]")
                
        