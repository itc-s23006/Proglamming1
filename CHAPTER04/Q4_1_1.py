def fib(n):
    """nより小さなフィボナッチ数列を列挙する"""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b


# テスト
n = 1000  # フィボナッチ数列の上限
fib(n)
