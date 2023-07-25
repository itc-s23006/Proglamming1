def concat_words(*args, separator="."):
    """任意の数の位置引数と区切り文字を受け取り、区切り文字でつなげる"""
    return separator.join(args)


result1 = concat_words("a", "b", "c", "d", separator="_")
result2 = concat_words("OSAKA", "okinawa", "AKITA", separator=" * ")
print(result1)
print(result2)
