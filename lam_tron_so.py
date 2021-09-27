import math
t = int(input())
while(t > 0):
    s = str(input())
    x = []
    for i in range(len(s)-1, -1, -1):
        x.append(ord(s[i])-48)
    for i in range(len(x)-1):
        if(x[i] >= 5):
            x[i+1]+=1
        x[i] = 0
    for i in range(len(x)-1, -1, -1):
        print(x[i], end='')
    print(end='\n')
    t -= 1