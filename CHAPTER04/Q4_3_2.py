def func_square(*args):
    results = []
    for n in args:
        results.append(n * n)
    return results


numbers = [2, 3, 8, 9]
print(func_square(*numbers))

many_numbers = list(range(100))
print(func_square(*many_numbers))
