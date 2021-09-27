n = int(input())
flat = True
a = list(map(int, input(). split()))
a.sort()
# if(a[0] != 1):
#     print(1)
# else:
for i in range(0, n-1):
        if(a[i+1]-a[i] != 1):
            print(str(a[i]+1))
            flat = False
            break
if(flat):
        print(a[n-1]+1)
