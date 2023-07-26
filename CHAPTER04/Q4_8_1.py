import time


def show_begin_end(func):
    """呼ばれた関数の始めと終わりを表示するデコレータ"""

    def deco_func(*args, **kwargs):
        """関数を実行する前と後にメッセージを表示"""
        print("== start")
        result = func(*args, **kwargs)
        print("== end")
        return result

    return deco_func


def sleep_for_a_while():
    """しばらく眠る"""
    print("Sleeping ..")
    time.sleep(2)  # sleep for a while; interrupt me!
    print("Done Sleeping")


sleep_for_a_while()


@show_begin_end
def sleep_for_a_while():
    """しばらく眠る"""
    print("Sleeping ..")
    time.sleep(2)  # sleep for a while
    print("Done Sleeping")


sleep_for_a_while()
