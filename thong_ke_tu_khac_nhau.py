t = int(input())
a = str("")
while t > 0:
    t-=1
    s = input().lower()
    for i in range(len(s)):
        if((s[i] >= '0' and s[i] <= '9') or (s[i] >= 'a' and s[i] <= 'z') or(s[i] >= 'A' and s[i] <= 'Z')):
            a += s[i]
        else:
            a += ' '
    a += ' '
a = a.lower().split()
b = []
c = []
for i in a:
    if i not in b:
        b.append(i)
    if a.count(i) not in c:
        c.append(a.count(i))

b.sort()
c.sort(reverse=True)
# # for i in b:
# #     print(i)
# for i in c:
#     print(i)
for i in  c:
    for j in b:
        if(a.count(j) == i):
            print(j, i) 

# for i in  range(len(c)):
#     for j in range(len(b)):
#         if(a.count(b[j]) == c[i]):
#             print(b[j], c[i])

#             break

