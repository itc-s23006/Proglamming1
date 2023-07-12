my_list = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]
my_list_6 = []
for s in my_list:
    if len(s) >= 6:
        my_list_6.append(s)
print(my_list_6)

# 5文字以上の単語を出力する場合
my_list = ["oita", "hokkaido", "okinawa", "osaka", "mie"]
my_list_5 = []
for s in my_list:
    if len(s) >= 5:
        my_list_5.append(s)
print(my_list_5)
