n = int(input())
s = str(n)
x = ""
dem = 0
for i in range(len(s)-1, -1, -1):
    x = x + s[i]
    dem+=1
    if(dem == 3 and i != 0):
        x = x + ','
        dem = 0
print(x[::-1])