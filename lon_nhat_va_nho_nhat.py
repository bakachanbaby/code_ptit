while 1:
    t = int(input())
    if(t == 0):
        break
    tmp = []
    while(t > 0):
        t-=1
        s = str(input())
        s = s.lstrip('0')
        tmp.append(s)
    tmp.sort()
    if(tmp[0] == tmp[len(tmp)-1]):
        print('BANG NHAU')
    else:
        mx = 0
        mn = 105
        for i in range(len(tmp)):
            mx = max(len(tmp[i]), mx)
            mn = min(len(tmp[i]), mn)
        tmp1 = []
        tmp2 = []
        for i in range(len(tmp)):
            if(mx == len(tmp[i])):
                tmp1.append(tmp[i])
            if(mn == len(tmp[i])):
                tmp2.append(tmp[i])
        tmp1.sort()
        tmp2.sort()
        print(min(tmp2), max(tmp1))
