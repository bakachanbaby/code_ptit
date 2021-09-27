t = int(input())
while t > 0:
    s = str(input())
    y = s[::-1]
    flat = 0
    for i in range(1, len(s)):
       
        if(abs(ord(s[i])-ord(s[i-1])) != abs(ord(y[i])-ord(y[i-1]))):
            flat = 1
            print('NO')
            break
    if(flat == 0):
        print('YES')
    t-=1