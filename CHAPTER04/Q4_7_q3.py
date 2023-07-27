def print_multiplication_table():
    for i in range(1, 10):
        for j in range(1, 10):
            result = i * j
            print(f"{result:2}", end="  ")
        print()  # 改行


if __name__ == "__main__":
    print_multiplication_table()
