a = []
t = 10
while t > 0:
    s = str(input()).split(' ')
    for i in range(len(s)):
        x = int(s[i])%42
        a.append(x)
    t -=len(s)
a.sort()
dem = 1
for i in range(len(a)-1):
    if(a[i] != a[i+1]):
        dem+=1
print(dem)
