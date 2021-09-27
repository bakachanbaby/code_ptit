t = int(input())
while t > 0:
    s = str(input())
    a = int(1)
    if s[len(s)-1] == s[1] and s[len(s)-2] == s[0]:
        print('YES')
    else :
        print('NO')
    t -= 1
