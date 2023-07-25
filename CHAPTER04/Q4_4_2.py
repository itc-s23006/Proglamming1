def vote(vote_num, party):
    print(f"{party}に投票します")
    return vote_num + 1


def reset_votes():
    print("投票箱を空にします")
    return 0


def check_votes(democrat_votes, republican_votes):
    print("民主党の得票数:", democrat_votes)
    print("共和党の得票数:", republican_votes)


# 初期の票の数
democrat_votes = 0
republican_votes = 0

# テスト
republican_votes = vote(republican_votes, "共和党")
democrat_votes = vote(democrat_votes, "民主党")
republican_votes = vote(republican_votes, "共和党")
check_votes(democrat_votes, republican_votes)

# 投票箱を空にする
democrat_votes = reset_votes()
republican_votes = reset_votes()
check_votes(democrat_votes, republican_votes)
