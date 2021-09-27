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

def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

t = int(input())
while t > 0:
    dem = 0
    n = int(input())
    for i in range(1, n):
        if uscln(n, i) == 1:
            dem +=1
    if NT(dem) :
        print('YES')
    else:
        print('NO')
    t -=1
    
