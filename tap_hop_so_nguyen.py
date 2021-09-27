def giao(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i] == b[j]):
                print(a[i], end=' ')
        
    print()

def hieuAB(a, b):
    for i in range(len(a)):
        flat = True
        for j in range(len(b)):
            if(a[i] == b[j]):
                flat = False
        if(flat):
            print(a[i], end=' ')
    print()

s = str(input()).split(' ')
n = int(s[0])
m = int(s[1])
a = list(map(int, input().strip().split()))[:n]
b = list(map(int, input().strip().split()))[:m]
a.sort()
b.sort()
A = []
B = []
for i in range(len(a)-1):
    if(a[i] != a[i+1]):
        A.append(a[i])
A.append(a[len(a)-1])

for i in range(len(b)-1):
    if(b[i] != b[i+1]):
        B.append(b[i])
B.append(b[len(b)-1])

A.sort()
B.sort()

giao(A, B)
hieuAB(A, B)
hieuAB(B, A)
