class Nigiri:
    def __init__(self):
        self.rice = True
        self.wasabi = False
        self.soy_sauce = False

    def show_attributes(self):
        print(
            "rice: {}, wasabi: {}, soy sauce: {}".format(
                self.rice, self.wasabi, self.soy_sauce
            )
        )


class Katsuo(Nigiri):
    def __init__(self):
        super().__init__()  # Nigiriクラスのコンストラクタを呼び出す
        self.top = "かつお"
        self.topping = "生姜とねぎ"
        self.price = 100

    def show_attributes(self):
        super().show_attributes()  # Nigiriクラスのshow_attributesメソッドを呼び出す
        print("topping: {}".format(self.topping))


# Katsuoクラスのインスタンスを作成
katsuo_nigiri = Katsuo()

# 属性を表示
katsuo_nigiri.show_attributes()
