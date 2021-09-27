s1 = str(input())
s2 = str(input())
n = int(input())
for i in range(len(s1)):
    if(int(i) == int(n-1)):
        print(s2, end='')
    print(s1[i], end='')
if(n > len(s1)):
    print(s2, end='')