from abc import ABC, abstractmethod
import math

class BasicShape(ABC):
    def __init__(self, name="Shape"):
        self._area = 0.0
        self._name = name

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @abstractmethod
    def calc_area(self):
        pass


class Circle(BasicShape):
    def __init__(self, x, y, r, n="Circle"):
        super().__init__(n)
        self._x_center = x
        self._y_center = y
        self._radius = r
        self.calc_area()

    def calc_area(self):
        self._area = math.pi * self._radius ** 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self.calc_area()


class Rectangle(BasicShape):
    def __init__(self, l, w, n="Rectangle"):
        super().__init__(n)
        self._length = l
        self._width = w
        self.calc_area()

    def calc_area(self):
        self._area = self._length * self._width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value
        self.calc_area()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self.calc_area()

class Square(Rectangle):
    def __init__(self, s, n="Square"):
        self._side = s
        super().__init__(s, s, n)
        self.name = n

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value
        self._length = value
        self._width = value
        self.calc_area()


def main():
    shapes = [
        Circle(0, 0, 4, "Circle_1"),
        Circle(0, 0, 9, "Circle_2"),
        Rectangle(10, 20, "Rectangle_1"),
        Rectangle(20, 30, "Rectangle_2"),
        Square(10, "Square")
    ]

    print("--- Polymorphism check ---")
    for shape in shapes:
        print(f"{shape.name} Area = {shape.area}")

    print("\n--- Getter/setter check ---")

    c = shapes[0]
    print(f"{c.name} Current: {c.radius} {c.area}")
    c.radius *= 2
    print(f"{c.name} Doubled: {c.radius} {c.area}")

    r = shapes[2]
    print(f"{r.name} Current: {r.length} {r.width} {r.area}")
    r.length *= 2
    r.width *= 2
    print(f"{r.name} Doubled: {r.length} {r.width} {r.area}")

    s = shapes[4]
    print(f"{s.name} Current: {s.side} {s.area}")
    s.side *= 2
    print(f"{s.name} Doubled: {s.side} {s.area}")


if __name__ == "__main__":
    main()