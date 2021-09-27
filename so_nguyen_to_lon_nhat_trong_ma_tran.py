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

n, m = map(int, input().split())
a = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
mx = 0
for i in range(n):
    for j in range(m):
        if(NT(a[i][j])):
            mx = max(mx, a[i][j])  
if(mx == 0):
    print("NOT FOUND")
else:
    print(mx)
    for i in range(n):
        for j in range(m):
            if(mx == a[i][j]):
                print("Vi tri [" + str(i) + "][" + str(j) + "]")