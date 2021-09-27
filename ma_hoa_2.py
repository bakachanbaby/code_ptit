
while(1):
    t = str(input())
    s = t.split()
    a = int(s[0])
    if(a == 0):
        break
    x = ""
    y = s[1]
    p = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','.']
    # ord: chuyển 1 kí tự thành int
    for i in range(len(y)):
        if(y[i] >= 'A' and y[i] <= 'Z'):
            k = ((ord(y[i])-65)+a)%28
        elif y[i] == '_':
            k = ((ord(y[i])-69)+a)%28
        elif y[i] == '.':
            k = ((ord(y[i])-19)+a)%28
        x += p[k]
    print(x[::-1])
    
