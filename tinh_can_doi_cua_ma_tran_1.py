n = int(input())
a = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
k = int(input())
sum1 = 0
sum2 = 0
for i in range(n):
    for j in range(n):
        if(j > i):
            sum1 +=a[i][j]
        elif(j < i):
            sum2 +=a[i][j]
if(abs(sum1-sum2) > k):
    print('NO')
    print(abs(sum1-sum2))
else:
    print('YES')
    print(abs(sum1-sum2))