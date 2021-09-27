s = str(input())
n = 0
for i in range(len(s)):
    n = n*2 + (ord(s[i])-48)
print("%o" %n)
