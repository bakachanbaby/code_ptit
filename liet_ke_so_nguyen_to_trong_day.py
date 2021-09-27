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
a = list(map(int, input(). split()))
for i in range(n):
    if(NT(a[i])):
        print(str(a[i]) + ' ' + str(a.count(a[i])))
        for j in range(i+1, n):
            if(a[i] == a[j]):
                a[j] = 1
