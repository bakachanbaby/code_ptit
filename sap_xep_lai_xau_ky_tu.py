t = int(input())
for i in range(1, t+1):
    s = str(input())
    x = str(input())
    S = sorted(s)
    X = sorted(x)
    if(S == X):
        print('Test '+ str(i) + ': YES')
    else:
        print('Test '+ str(i) + ': NO')
        