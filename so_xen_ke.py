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
def tn(s):
    y = str(s)
    x = y[::-1]
    z = len(y)
    if(x == y and z > 1):
        return True
    return False
def soChuSo(s):
    if(len(s)%2!=0):
        return True
    return False

def soDauTien(s):
    if(s[0] != s[1]):
        return True
    return False


def index(s):
    for i in range(0, len(s)-2, 2):
        if(s[i] != s[i+2]):
            return False
    return True
    

t = int(input())
while(t > 0):   
    n = str(input())
    if(soChuSo(n) and soDauTien(n) and index(n)):
        print('YES')
    else:
        print('NO')
    t -=1