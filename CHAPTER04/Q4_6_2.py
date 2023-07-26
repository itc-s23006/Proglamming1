import random

# ランダムな生徒データを生成
num_students = 10
names = ["生徒" + str(i) for i in range(1, num_students + 1)]
heights = [random.randint(150, 189) for _ in range(num_students)]
weights = [random.randint(40, 89) for _ in range(num_students)]
students_data = list(zip(names, heights, weights))

# 身長順に並べ替え
students_data_by_height = sorted(students_data, key=lambda x: x[1])

# 体重順に並べ替え
students_data_by_weight = sorted(students_data, key=lambda x: x[2])

# 結果の表示
print("生徒データ（身長順）：")
print(students_data_by_height)

print("\n生徒データ（体重順）：")
print(students_data_by_weight)
