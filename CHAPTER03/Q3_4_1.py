for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# continueをbreakに変える
for i in range(10):
    if i % 2 == 0:
        break
    print(i)

# 偶数を表示
for H in range(28):
    if H % 2 != 0:
        continue
    print(H)
