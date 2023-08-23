# 100万行のテキストファイルを生成する
with open("large_file.txt", "w") as file:
    for i in range(1000000):
        file.write(f"This is line {i+1}\n")

# 生成したファイルの最初の3行を表示する
with open("large_file.txt", "r") as file:
    for _ in range(3):
        line = file.readline().strip()
        print(line)
