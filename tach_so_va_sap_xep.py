t = int(input())
a = []

while t > 0:
    t-=1
    s = str(input())
    sum = str("")
    for i in range(len(s)):
        if(s[i] >= '0' and s[i] <= '9'):
            sum = sum + s[i]
        elif(len(sum) > 0):
            a.append(int(sum))
            sum = ""
    if(len(sum) > 0):
        a.append(int(sum))
a.sort()

for i in range(len(a)):
    
    print(a[i])
