vote_num = 0


def vote():
    print("投票します")
    global vote_num
    vote_num += 1


def reset_box():
    global vote_num
    print("箱を空にします")
    vote_num = 0


def check_box():
    global vote_num
    print("票の数は{}です".format(vote_num))


# 投票1回
vote()
# 現在の票の数を表示
check_box()
# 箱を空にする
reset_box()
# 投票28回
for i in range(28):
    vote()
# 現在の票の数を表示
check_box()

# 箱を空にする
reset_box()
# 現在の票の数を表示
check_box()
