import calendar


def display_calendar(year, month):
    cal = calendar.month(year, month)
    print(cal)


# ユーザーから年と月を入力してもらう
year = int(input("年を入力してください: "))
month = int(input("月を入力してください: "))

# カレンダーを表示する
display_calendar(year, month)
