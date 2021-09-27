def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

s = input().split(' ')
n = int(s[0])
k = int(s[1])
dem = 0
for i in range(10**(k-1), 10**k - 1, 1):
    if(uscln(i, n) == 1):
        dem+=1
        print(i, end=' ')
    if(dem == 10):
        print(end='\n')
        dem = 0

