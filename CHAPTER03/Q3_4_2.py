numbers = [1, 1, 2, 3, 5, 8, 13, 21]
x = 0
for n in numbers:
    if n > 10:
        break
    x += n
print(x)

# n > 10の場合
numbers = [2, 3, 8, 9, 18, 21, 29, 38]
K = 0
for n in numbers:
    if n > 10:
        break
    else:
        K += n
print(K)
