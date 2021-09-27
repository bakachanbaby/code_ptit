def convert_number(n, b):
    sb = ""
    m = 0
    tmp = n
    while (tmp > 0):
        if (b > 10):
            m = tmp % b
            if (m >= 10):
                sb = sb + str(chr(55 + m))
            else:
                sb = sb + str(m)
        else:
            sb = sb + str(tmp % b)
        tmp = int(tmp / b)
    return "".join(reversed(sb))  # đảo ngược chuỗi sb


t = int(input())
while t > 0:
    t -= 1
    s = str(input()).split(' ')
    n = int(s[0])
    b = int(s[1])
    print(convert_number(n, b))
