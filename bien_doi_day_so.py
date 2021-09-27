s = str("1 2 3 4").split(' ')
a = []
for i in range(4):
    a.append(s[i])
while(1):
    a = list( map( int , input().strip().split() ) ) [:4]
    if (a[0] == 0 and a[1] == a[0] and a[2] == a[1] and a[3] == a[2]): 
        break
    dem = 0
    while(1):
        if(a[1] == a[0] and a[2] == a[1] and a[3] == a[2]):
            break
        else:
            dem +=1
            x = a[0]
            for i in range(3):
                a[i] = abs(a[i]-a[i+1])
            a[3] = abs(a[3]-x)
    print(dem)

