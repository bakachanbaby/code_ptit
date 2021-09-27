n = int(input())
dem = 0
a = list(map(int, input(). split()))

for i in range(0, n-1):
    if(a[i+1] != a[i]):
        dem +=1
print(dem)