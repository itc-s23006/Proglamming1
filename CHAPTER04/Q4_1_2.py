def fib2(n):
    """nより小さなフィボナッチ数列をリストで返す"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


# テスト
n = 1000  # フィボナッチ数列の上限
fibonacci_list = fib2(n)
print(fibonacci_list)
