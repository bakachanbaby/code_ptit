t = int(input())
while t > 0:
    t-=1
    s = str(input()).split()
    n = int(s[0])
    p = int(s[1])
    x = 0
    while n > 0:
        n = int(n/p)
        x += n
    print(x)