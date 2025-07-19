# function: 二维向量类
# author: fuyuan360


class Vector:

    def __init__(self, x, y) -> None:
        """
        初始化二维向量
        :param x: x坐标值
        :param y: y坐标值
        """
        self.x: int = int(x)
        self.y: int = int(y)

    def __repr__(self) -> str:
        return f"Vector({self.x!r}, {self.y!r})"

    def __add__(self, other) -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    vector1: Vector = Vector(1, 2)
    vector2: Vector = Vector(3, 4)
    print(vector1 + vector2)
