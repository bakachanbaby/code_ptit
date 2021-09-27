def fibonacci(n):
    f0 = 0;
    f1 = 1;
    fn = 1;
    if (n < 0):
        return -1;
    elif (n == 0 or n == 1):
        return n;
    else:
        for i in range(2, n):
            f0 = f1;
            f1 = fn;
            fn = f0 + f1;
        return fn;
 
t = int(input())
while(t > 0):
    s = str(input())
    x = s.split()
    a = int(x[0])
    b = int(x[1])
    sb = "";
    for i in range(a, b+1):
        sb = sb + str(fibonacci(i)) + " ";
    print(sb)
    t -=1