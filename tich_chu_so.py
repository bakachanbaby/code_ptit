t = int(input())
while t > 0:
    t-=1
    s = str(input())
    sum = 1
    for i in range(len(s)):
        if s[i] != '0':
            sum *= (ord(s[i])-48)
    print(sum)