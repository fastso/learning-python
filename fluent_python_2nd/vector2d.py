import math
from array import array


class Vector2d:
    # クラス変数　Vector2d instance と bytes の変換に使用する。
    typecode = 'd'

    def __init__(self, x, y):
        # float()を使用することで、早期に不適切な引数を検出できる。
        self.__x = float(x)
        self.__y = float(y)

    @property  # getter
    def x(self):
        return self.__x

    @property  # getter
    def y(self):
        return self.__y

    def __iter__(self):
        # イテラブル化する。これでunparkを機能させる。
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        # イテラブルなので、*selfはxとyをformatに渡す。
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        # イテラブルなVector2dから、簡単に順序付きペアのタプルを生成する。
        return str(tuple(self))

    def __bytes__(self):
        # typecodeをbytesに変換し連結する。
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    @classmethod
    def from_bytes(cls, octets):
        """
        bytesからVector2dを生成する。
        @classmethodのため直接クラスから呼び出す。self引数ではなく、クラスcls引数が渡される。
        :param octets:
        :return:
        """
        # 1バイト目からtypecodeを取得する。
        typecode = chr(octets[0])
        # octetsバイナリ列からmemmapを作成し、typecodeを使ってキャストする。
        memv = memoryview(octets[1:]).cast(typecode)
        # キャストしたmemvを必要な引数のペアにunpackして、Vector2dのコンストラクタに渡してインスタンスを生成する。
        return cls(*memv)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        # __hash__と__eq__を実装すると、setに追加できる。
        return hash((self.x, self.y))

    def __abs__(self):
        # xとyで形成される直角三角形の斜辺の長さを計算する。
        return math.hypot(self.x, self.y)

    def __bool__(self):
        # absが0の場合はFalseを返す。
        return bool(abs(self))

    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self)
        return '({}, {})'.format(*components)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2d(x, y)

    def __mul__(self, scalar):
        return Vector2d(self.x * scalar, self.y * scalar)

    def angle(self):
        return math.atan2(self.y, self.x)


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    # 3.0 4.0

    x, y = v1
    print(x, y)
    # 3.0 4.0

    # v1
    # Vector2d(3.0, 4.0)

    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)
    # True

    print(v1)
    # (3.0, 4.0)

    octets = bytes(v1)
    print(octets)
    # b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'

    print(abs(v1))
    # 5.0

    print(bool(v1), bool(Vector2d(0, 0)))
    # True False

    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)
    print(hash(v1), hash(v2))
    print({v1, v2})

