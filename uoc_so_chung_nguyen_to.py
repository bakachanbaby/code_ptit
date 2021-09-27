import math
def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

def tong(n):
    sum = 0;
    while (n > 0):
        sum = sum + n % 10;
        n = int(n / 10);
    return sum

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
    x = s.split()
    a = int(x[0])
    b = int(x[1])
    y = uscln(a, b)
    y = tong(y)
    if(NT(y)):
        print('YES')
    else:
        print('NO')
    t-=1

