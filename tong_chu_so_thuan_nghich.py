def tn(s):
    y = str(s)
    x = y[::-1]
    z = len(y)
    if(x == y and z > 1):
        return True
    return False

def tong(s):
    sum = 0
    for i in range(len(s)):
        sum += (ord(s[i]) - 48)
    if(tn(sum)):
        return True
    return False

t = int(input())
while(t > 0):
    n = str(input())
    if(tong(n)):
        print('YES')
    else:
        print('NO')
    t -=1