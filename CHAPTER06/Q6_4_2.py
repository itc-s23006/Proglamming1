def gen_prime():
    yield 2  # 最初の素数を返す
    primes = [2]  # 素数を保持するリスト

    num = 3
    while True:
        is_prime = True

        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
            yield num

        num += 2  # 奇数のみをチェックする


# 最初の10個の素数を生成して表示する
prime_generator = gen_prime()
for _ in range(10):
    print(next(prime_generator))
