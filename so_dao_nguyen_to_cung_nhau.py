import math
def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

def NT(n):
    if(n<2):  # neu n nho hon 2 thi tra ve False
        return False
    i=2
    while i <= math.sqrt(n):
        if(n%i == 0): # neu n chia het cho bat ki so nao thi tra ve Fasle
            return False
        i+=1
    return True 

t = int(input())
while t > 0:
    s = str(input())
    S = s[::-1]
    n = int(s)
    m = int(S)
    if(uscln(n, m ) == 1):
        print('YES')
    else :
        print('NO')
    t-=1

