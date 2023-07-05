from decimal import Decimal, getcontext

a = 12
b = 55

getcontext().prec = 18  # 有効桁数を設定

result = Decimal(a) / Decimal(b)

print(result)
