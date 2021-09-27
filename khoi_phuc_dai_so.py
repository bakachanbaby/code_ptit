n = int(input())
a = []
for i in range(n):
    hang = list(map(int, input().split()))
    a.append(hang)  

if n == 2:
    print(1, a[0][1] - 1)
else:
    arr0 = int((a[0][1] + a[0][2] - a[1][2]) / 2)
    print(arr0, end=' ')
    for i in range(1, n):
        print(a[0][i] - arr0, end=' ')
