t = int(input())
while t > 0:
    s = str(input())
    a = int(1)
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            a = 0
            print('NO')
            break
    if a == 1:
        print('YES')
    t = t - 1
