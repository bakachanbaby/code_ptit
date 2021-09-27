t = int(input())
while t > 0:
    s = str(input())
    x = ""
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            for j in range(1, int(s[i])):
                x = x + s[i-1]
        else:
                x = x + s[i]
    print(x)
    t = t - 1
