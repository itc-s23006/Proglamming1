# 1から20まで表示する場合
import pickle

with open("test1.pkl", "wb") as f:
    my_list = list(range(1, 21))
    pickle.dump(my_list, f)
    print(my_list)
