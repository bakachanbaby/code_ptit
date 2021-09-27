t = int(input())
while t > 0:
    s = str(input())
    dem = 0
    for i in range(len(s)):
        if s[i] != '4' and s[i] != '7':
            dem = 1
            print('NO')
            break
    if dem == 0:
        print('YES')
    t-=1
