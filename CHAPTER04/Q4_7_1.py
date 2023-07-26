def make_addfunc():
    def add(x, y):
        return x + y

    return add


adder = make_addfunc()
answer = adder(44, 44)
print(answer)
