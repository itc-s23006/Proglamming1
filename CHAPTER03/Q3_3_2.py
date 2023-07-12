my_list = [1, 1, 2, 3, 5, 8, 13]
x = 0
for n in my_list:
    if n % 2 != 0:
        x += n
print(x)

# 3で割り切れるか確認する時の処理
my_list = [2000, 2001, 2004, 1992, 1991]
x = 0
for n in my_list:
    if n % 3 != 0:
        x += n
        x += 2454
print(x)
