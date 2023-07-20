def fib(n):
    """nより小さなフィボナッチ数列を列挙する"""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b


# テスト
n = 1000  # フィボナッチ数列の上限
fib(n)

# *の場合(1から)


def fib(K):
    """nより小さいフィボナッチ数列を列挙する"""
    A, B = 1, 2
    while A < K:
        print(A, end=" ")
        A, B = B, A * B


K = 500
fib(K)
