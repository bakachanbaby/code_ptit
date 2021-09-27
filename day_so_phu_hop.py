t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input(). split()))
    b = list(map(int, input(). split()))
    flat = 1
    a.sort()
    b.sort()
    for i in range(len(a)):
        if(a[i] > b[i]):
            flat = 0
            print('NO')
            break
    if(flat == 1):
        print('YES')
    t -= 1
