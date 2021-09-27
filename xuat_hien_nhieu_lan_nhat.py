t = int(input())
while t > 0:
    n = int(input())
    dem = 0
    x = int(0)
    flat = 1
    a = list(map(int, input(). split()))
    a.sort()
    # print(n/2)
    for i in range(len(a)):
        if(a.count(a[i]) >= n/2):
            flat = 0
            print(a[i])
            break
    if(flat == 1):
        print('NO')
    # for i in range(0, n):
    #     dem = 1
    #     for j in range(i+1, n):
    #         if(a[i] == a[j]):
    #             dem += 1
    #             x = a[j]
    #     if(dem > n/2):
    #         print(x)
    #         flat = 0
    #         break
    # if(flat == 1):
    #     print('NO')
    t -= 1
