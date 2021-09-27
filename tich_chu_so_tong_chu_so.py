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
    sum = 1
    flat = True
    for i in range(0, len(s), 2):
        if((ord(s[i])-48) != 0):
            sum *= (ord(s[i])-48)
            flat = False
    if(flat):
        return 0
    else:
        return sum
def indexLe(s):
    sum = 0
    for i in range(1, len(s), 2):
        sum += (ord(s[i])-48)
    return sum

t = int(input())
while(t > 0):   
    n = str(input())
    print(indexChan(n), end=' ')
    print(indexLe(n), end='\n')
    t -=1