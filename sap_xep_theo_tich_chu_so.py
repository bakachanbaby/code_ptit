def tong(n):
    sum = int(1)
    while n > 0:
        sum *= n % 10
        n = int(n / 10)
    return sum


def size(n):
    s = str(n)
    return len(s)


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input(). split()))
    a.sort()
    b = []
    for i in range(n):
        b.append(tong(a[i]))
    b.sort()
    for i in range(n):
        for j in range(n):
            if(b[i] == tong(a[j]) and a[j] != 0):
                print(a[j], end=' ')
                a[j] = 0
                break
    
    print()
