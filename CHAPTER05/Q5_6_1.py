a = {x for x in "abcabcabc" if x not in "ab"}
b = {y for y in "abcabcabc" if y not in "bc"}
a | b
print(a | b)

# KRを出力する場合
A = {z for z in "KIRI" if z not in "KI"}
B = {v for v in "KIRI" if v not in "RI"}
print(A | B)
