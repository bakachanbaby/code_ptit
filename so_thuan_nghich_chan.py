def tn(s):
    x = s[::-1]
    if(s == x):
        return True
    return False

def chan(s):
    for i in range(len(s)):
        if(ord(s[i]) % 2 != 0):
            return False
    return True

def so(s):
    if len(s) % 2 == 0:
        return True
    return False

t = int(input())
while(t > 0):
    n = int(input())
    s = str("")
    for i in range(22, n):
        if tn(str(i)) and chan(str(i)) and so(str(i)):
            s += str(i) + ' '
    print(s)
    t -=1