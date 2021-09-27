t = int(input())
while t > 0:
    t-=1
    s = input().split()
    n, m, k = int(s[0]), int(s[1]), int(s[2])
    a = list(map(int, input().strip().split()))[:n]
    b = list(map(int, input().strip().split()))[:m]
    c = list(map(int, input().strip().split()))[:k]
    check, i, j, p = 0, 0, 0, 0
    while i < n and j < m and p < k:
        if a[i] == b[j] and b[j] == c[p]:
            print(a[i], end=' ')
            check = 1
            i, j, p = i+1, j+1, p+1
        elif a[i] < b[j]:   i += 1
        elif b[j] < c[p]:   j += 1
        else :p += 1
    if(check == 0):
        print('NO', end='')
    print()