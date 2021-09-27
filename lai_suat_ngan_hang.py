t = int(input())
while(t > 0):
    s = input().split(' ')
    n = float(s[0])
    x = float(s[1])
    x /=100
    m = float(s[2])
    dem = int(0)
    while(n < m):
        n += n*x
        dem+=1
    print(str(dem))
    t-=1