name_age = {"tanaka": 35, "satou": 25, "suzuki": 27}


def dict_info(dict_tbl, key):
    try:
        return dict_tbl[key]
    except:
        return "key is not found"


print(dict_info(name_age, "satou"))
print(dict_info(name_age, "yamada"))

#
Name_Age = {"kiyuna": 28, "kaki": 22, "tamaki": 37}


def ei_suuji(ei_number, key):
    try:
        return ei_number[key]
    except:
        return "key is not found"


print(ei_suuji(Name_Age, "maeda"))
print(ei_suuji(Name_Age, "kaki"))
