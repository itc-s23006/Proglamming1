class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_perimeter(self):
        return 2 * (self.width + self.height)

    def calc_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # 正方形の場合、幅と高さが同じ


# 長方形クラスのインスタンスを作成
rectangle = Rectangle(width=5, height=10)
print("長方形の周の長さ:", rectangle.calc_perimeter())
print("長方形の面積:", rectangle.calc_area())

# 正方形クラスのインスタンスを作成
square = Square(side=7)
print("正方形の周の長さ:", square.calc_perimeter())
print("正方形の面積:", square.calc_area())
