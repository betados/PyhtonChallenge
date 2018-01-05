# a = [1, 11, 21, 1211, 111221,
import math

def tri2dec(tri):
    salida = 0
    for i, c in enumerate(reversed(str(tri))):
        mult = math.pow(3, i)
        salida += int(c) * mult
        print
    return int(salida)

def ternary(n):
    e = n//3
    q = n%3
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return ternary(e) + str(q)

# http://www.pythonchallenge.com/pc/return/bull.html

print(ternary(4))
print(tri2dec(11))

a = [1, 11, 21, 1211, 111221]
a = 1
# b = [1]
# for _ in range(5):
#     b.append(dec2tri(tri2dec(b[-1])))
# print(b)
# a = [1, 2, 2, 4, 6]
# for _ in range(27):
#     a.append(a[-1] + a[-2])
#
# print(a)
# print(a[30])


