import math

def tong(n):
    sum = 0;
    while (n > 0):
        sum = sum + n % 10;
        n = int(n / 10);
    if(sum % 10 == 0):
        return True
    return False

def cachNhau(n):
    s = str(n)
    for i in range(len(s)-1):
        if(abs(ord(s[i])-ord(s[i+1])) != 2):
            return False
    return True
t = int(input())
while t > 0:
    n = int(input())
    if(tong(n) and cachNhau(n)):
        print('YES')
    else:
        print('NO')
    t-=1

