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

t = int(input())
while t > 0:
    dem = int(0)
    n = int(input())
    s = int(n)
    print(1, end='')
    for i in range(2, int(math.sqrt(n))):
        dem = 0
        while(s % i == 0 ):
            dem+=1
            s= int(s/i)
        if(dem > 0 ):
            print(" * " +  str(i) + "^" + str(dem), end='')
    if(s > 1):
        print(" * " +  str(s) + "^" + str(1), end='')
    print()
    t -=1
    
