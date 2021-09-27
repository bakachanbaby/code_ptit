s = input().split()
a = int(s[0])
k = int(s[1])
n = int(s[2])
flat = True
for i in range(k-a, n-a+1, k):
    if((a + i <= n) and ((a+i) % k == 0) and i > 0):
        flat = False
        print(i, end=' ')

if(flat):
    print(-1)
