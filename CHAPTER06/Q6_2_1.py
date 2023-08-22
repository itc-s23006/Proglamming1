class Cylinder:
    """円柱クラス"""

    pi = 3.14

    def __init__(self, radius=1, height=1):
        """コンストラクタ"""
        self.radius = float(radius)
        self.height = float(height)

    def calc_base_area(self):
        """底面積を計算するメソッド"""
        pi = Cylinder.pi  # クラス変数のpiを参照
        r = self.radius
        return pi * r * r

    def calc_side_area(self):
        """側面積を計算するメソッド"""
        pi = Cylinder.pi  # クラス変数のpiを参照
        r = self.radius
        h = self.height
        return 2 * pi * r * h

    def calc_surface_area(self):
        """表面積を計算するメソッド"""
        c = self.calc_base_area()
        s = self.calc_side_area()
        return 2 * c + s

    def calc_volume(self):
        """体積を計算するメソッド"""
        c = self.calc_base_area()
        h = self.height
        return c * h

    def show_results(self):
        """結果を出力するメソッド"""
        r = self.radius
        h = self.height
        s = self.calc_surface_area()
        v = self.calc_volume()
        print("半径: {}, 高さ: {}, 表面積: {}, 体積: {}".format(r, h, s, v))  # 行が長いので改行しました


# インスタンスの作成と結果の表示
cylinder = Cylinder(radius=5, height=10)
cylinder.show_results()
