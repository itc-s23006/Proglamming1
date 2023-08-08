list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [x if x % 2 == 0 else None for x in list1]
print(result)

# x%3 の時
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result2 = [x if x % 3 == 0 else None for x in list2]
print(result2)
