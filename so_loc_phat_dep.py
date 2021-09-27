s = str(input())
s = s + "   "
flat = False
i = 0
while(i < len(s)-3):
    if(s[i] == '6' and s[i+1] == '8' and s[i+2] == '8'):
        i+=3
    elif(s[i] == '6' and s[i+1] == '8'):
        i+=2
    elif(s[i] == '6'):
        i+=1
    else:
        flat = True
        break
if(flat):
    print('NO')
else:
    print('YES')