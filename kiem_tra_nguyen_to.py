import math


def NT(n):
    if(n < 2):  # neu n nho hon 2 thi tra ve False
        return False
    i = 2
    while i <= math.sqrt(n):
        if(n % i == 0):  # neu n chia het cho bat ki so nao thi tra ve Fasle
            return False
        i += 1
    return True


s = input().split()
n, m = int(s[0]), int(s[1])
a = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)

for i in range(n):
    for j in range(m):
        if NT(a[i][j]):
            a[i][j] = 1
        else:
            a[i][j] = 0
        print(a[i][j], end=' ')
    print(end='\n')
