n = int(input())
a = list(map(int, input().strip().split()))[:n]
mn = 1000000
index = a[0]
for i in range(0, n):
    sum = 0
    for j in range(0, n):
        sum +=(abs(a[i]-a[j]))
    if(sum < mn):
        mn = sum
        index = a[i]
print(mn, index)