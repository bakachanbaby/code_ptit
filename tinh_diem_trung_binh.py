from typing import FrozenSet


n = int(input())
a = list(map(float,input(). split ()))
a.sort()
dem = 0
mx = a[n-1]
mi = a[0]
sum = float(0)
for i in range(len(a)):
    if(a[i] != mx and a[i] != mi):
        sum +=a[i]
        dem +=1
sum/=dem
print(format(sum, '.2f'))


