# max = 13のとき
functions = [sum, min, max]
number_list = range(2, 14)
for func in functions:
    print("Function: {}, Result: {}".format(func.__name__, func(number_list)))
