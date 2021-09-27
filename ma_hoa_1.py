t = int(input())
while t > 0:
    s = str(input())
    x = ""
    dem = 1
    for i in range(len(s)-1):
        if(s[i] == s[i+1]):
            dem += 1
        else: 
            x = x + str(dem) + s[i]
            dem = 1
    # if(s[len(s)-2] == s[len(s)-1]):
    #     dem+=1
    # Cộng thêm phần tử cuối
    x = x + str(dem) + s[len(s)-1]
    print(x)
    t = t - 1
