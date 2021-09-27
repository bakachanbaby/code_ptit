def sum(n):
    tong = 0
    while(n > 0):
        tong += n % 10
        n = int(n/10)
    return tong


def handling(n):
    tong = 0
    if len(n) < 2:
        return 0
    for i in n:
        if i == '-':
            tong += (ord(i) - ord('0'))
        else:
           tong += int(i)
    dem = 1
    while(tong >= 10):
        tong = sum(tong)
        dem += 1
    return dem


n = input()
print(handling(n))
