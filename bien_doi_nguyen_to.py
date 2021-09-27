import math
danh_dau=[True]*(10000+1) 
danh_dau[0] = False
danh_dau[1] = False
for i in range(2,1000+1): 
    if danh_dau[i]: 
            
        for j in range(i*i,10000+1,i): 
            danh_dau[j]=False 

# primes=[]
# for i in range(2,10000+1): 
#     if danh_dau[i]: 
#         primes.append(i)

n = int(input())
a = list(map(int, input().strip().split()))[:n]
b = []
for i in range(len(a)):
    x = a[i]
    dem1 = 0
    while(danh_dau[x] == False):
        x+=1
        dem1+=1
    x = a[i]
    dem2 = 0
    while(danh_dau[x] == False):
        x-=1
        dem2+=1
    # print(dem1, dem2)
    b.append(min(dem1, dem2))

print(max(b))