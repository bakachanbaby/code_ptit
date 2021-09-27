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
a = list(map(int, input().strip().split()))[:n]
b = []
for i in a:
    if i not in b:
        b.append(i)

flat = True
for i in range(len(b)):
    sum1 = 0
    sum2 = 0
    for j in range(i+1):
        sum1 += b[j]
    for j in range(i+1, len(b)):
        sum2 += b[j]
    if(NT(sum1) and NT(sum2)):
        print(i)
        flat = False
        break
if(flat):
    print('NOT FOUND')
