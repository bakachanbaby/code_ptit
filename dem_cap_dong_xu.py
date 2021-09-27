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

n = int(input())
a = []
for i in range(n):
    x = input()
    x = list(x)
    a.append(x)
dem = 0
for i in range(n):
    for j in range(n-1):
        for l in range(j+1, n):
            if(a[i][j] == a[i][l] and a[i][j] == 'C'):
                dem+=1

for i in range(n):
    for j in range(n-1):
        for l in range(j+1, n):
            if(a[j][i] == a[l][i] and a[j][i] == 'C'):
                dem+=1

print(dem)