
import sys


def prevNum(s, n):
	vt = -1

	for i in range(n - 2, -1, -1):
		if int(s[i]) > int(s[i + 1]):
			vt = i
			break

	tmp = -1
	for i in range(n - 1, vt, -1):
	    if (tmp == -1 and ord(s[i]) < ord(s[vt])):
		    tmp = i
	    elif (vt > -1 and ord(s[i]) >= ord(s[tmp]) and ord(s[i]) < ord(s[vt])):
		    tmp = i

	if vt == -1:
		return "" . join("-1")
	else:
	    (s[vt], s[tmp]) = (s[tmp], s[vt])
	return "" . join(s)


t = int(input())
while t > 0:
    s = str(input())
    s = prevNum(list(s), len(s))
    if(s[0] == '0'):
        print(-1)
    else:
        print(s)
    t -= 1
