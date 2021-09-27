t = int(input())
while t > 0:
    s = str(input())
    a = int(1)
    if s[len(s)-1] == '6' and s[len(s)-2] == '8':
        print('YES')
    else :
        print('NO')
    t -= 1
