import math
danh_dau=[True]*(100000+1) 
for i in range(2,400+1): 
    if danh_dau[i]: 
            
        for j in range(i*i,100000+1,i): 
            danh_dau[j]=False 
primes=[]
for i in range(2,100000+1): 
    if danh_dau[i]: 
        primes.append(i)

s = str(input())
t = s.split()
n = int(t[0])
x = int(t[1])
print(x, end=' ')
sum = int(x)
for i in range(0,n):
    sum +=primes[i]
    print(sum, end=' ')

