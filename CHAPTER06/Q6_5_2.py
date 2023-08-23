import my_math2

x = 2
y = 5
result = my_math2.my_pow(x, y)
expected_result = 32

if result == expected_result:
    print(f"Test passed: {x} の {y} 乗は {result} です。")
else:
    print(f"Test failed: 期待結果は {expected_result} ですが、実際の結果は {result} でした。")
