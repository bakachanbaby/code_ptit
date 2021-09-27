t = int(input())
while t > 0:
    t-=1
    s = str(input())
    sum = 0
    for i in range(len(s)):
        sum = (sum*10+(ord(s[i])-48))%3
    if(sum%3==0):
        print('YES')
    else:
        print('NO')