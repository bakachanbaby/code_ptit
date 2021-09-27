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

def size(n):
    sum = 0
    for i in range(len(n)):
        if(NT(ord(n[i])-48)):
            sum+=1
    if(sum > len(n)/2):
  
        return True
    return False

    
t = int(input())
while(t > 0):   
    n = str(input())
    if(NT(len(n)) and size(n)):
        print('YES')
    else:
        print('NO')
    t -=1