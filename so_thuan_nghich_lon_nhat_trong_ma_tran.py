# def TN(n):
#     n = str(n)
#     x = n[::-1]
#     if(x == n and len(n) > 1):
#         return True
#     return False

# n, m = map(int, input().split())
# a = []
# for i in range(n):
#     x = list(map(int, input().split()))
#     a.append(x)
# mx = -1
# for i in range(n):
#     for j in range(m):
#         if(TN(a[i][j])):
#             mx = max(mx, a[i][j])  
# if(mx == -1):
#     print("NOT FOUND")
# else:
#     print(mx)
#     for i in range(n):
#         for j in range(m):
#             if(mx == a[i][j]):
#                 print("Vi tri [" + str(i) + "][" + str(j) + "]")
def TN(n):
    n = str(n)
    x = n[::-1]
    if(x == n and len(n) > 1):
        return True
    return False

n, m = map(int, input().split())
a = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
mx = -1
for i in range(n):
    for j in range(m):
        if(TN(a[i][j])):
            mx = max(mx, a[i][j])  
if(mx == -1):
    print("NOT FOUND")
else:
    print(mx)
    for i in range(n):
        for j in range(m):
            if(mx == a[i][j]):
                print("Vi tri [" + str(i) + "][" + str(j) + "]")