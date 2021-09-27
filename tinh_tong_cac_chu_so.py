t = int(input())
while t > 0:
    t-=1
    s = str(input())
    sum = 0
    b = []
    for i in range(len(s)):
        if(s[i] >= '0' and s[i] <= '9'):
            sum += (ord(s[i])-48)
        else:
            b.append(s[i])
    b.sort()
    for i in b:
        print(i, end='')
    print(sum)