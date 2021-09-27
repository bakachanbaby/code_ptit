import math
def NT(n):
    if(n<2):  # neu n nho hon 2 thi tra ve False
        return False
    i=2
    while i <= math.sqrt(n):
        if(n%i == 0): # neu n chia het cho bat ki so nao thi tra ve Fasle
            return False
        i+=1
    return True 

n = int(input())
a = list(map(int, input().strip().split()))[:n]
b = []
for i in range(len(a)):
    if(NT(a[i])):
        b.append(a[i])
b.sort()
x = 0
for i in range(len(a)):
    if(NT(a[i])):
        print(b[x], end=' ')
        x+=1
    else:
        print(a[i], end=' ')