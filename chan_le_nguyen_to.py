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

def indexChan(s):
    for i in range(0, len(s)-1, 2):
        if((ord(s[i])-48) % 2 != 0):
            return False
    return True
    
def indexLe(s):
    for i in range(1, len(s), 2):
        if((ord(s[i])-48) % 2 == 0):
            return False
    return True

def tong(s):
    sum = 0
    for i in range(len(s)):
        sum += ord(s[i])-48
    if(NT(sum)):
        return True
    return False
t = int(input())
while(t > 0):   
    n = str(input())
    if(indexLe(n) and indexChan(n) and tong(n)):
        print('YES')
    else:
        print('NO')
    t -=1