import math
def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

s = input().split(' ')
n = int(s[0])
m = int(s[1])

for i in range(n, m-1):
    for j in range(i+1, m):
        if(math.gcd(i, j)==1):
            for l in range(j+1, m+1):
                if(math.gcd(i, l) == 1 and math.gcd(j, l) == 1):
                    print('(' + str(i) + ', ' + str(j) + ', ' + str(l) + ')')
                
