A = {x for x in range(21)}
print(A)
B = {x for x in range(21) if x % 2 == 0}
print(B)
C = A - B
print(C)

# 2, 3, 7, 8の倍数を消去
a = {y for y in range(23)}
print(a)
b = {y for y in range(23) if y % 2 == 0}
print(b)
c = {y for y in range(23) if y % 3 == 0}
print(c)
d = {y for y in range(23) if y % 7 == 0}
print(d)
e = {y for y in range(23) if y % 8 == 0}
print(e)
f = a - b - c - d - e
print(f)
