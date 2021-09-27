s = str(input())
if(len(s) == 1):
    print(0)
else:

    while(len(s) > 1):
        tmp1 = 0
        tmp2 = 0
        n = int(len(s)/2)
        for i in range(n):
            tmp1 = tmp1 * 10 + (ord(s[i])-48)
        for i in range(n, len(s)):
            tmp2 = tmp2 * 10 + (ord(s[i])-48)
        s = str(tmp1+tmp2)
        print(s)