import math


class Figure():
    sides_count = 0

    def __init__(self, colors: tuple, *sides_qty: int, filled=False):
        if self.__is_valid_sides(*sides_qty):
            self.__sides = [*sides_qty]
        else:
            self.__sides = [1 for _ in range(0, self.sides_count)]
        if self.__is_valid_color(*colors):
            self.__color = [*colors]
        else:
            self.__color = [0, 0, 0]
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r > 255 or r < 0 or g > 255 or g < 0 or b > 255 or b < 0:
            return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
           self.__color = [r, g, b]
        else:
            print(f'Параметры не могут превышать значение 255 или быть меньше 0')

    def __is_valid_sides(self, *args):
        for side in args:
            if side <= 0 or not isinstance(side, int):
                return False
        if len(args) != self.sides_count:
            return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            print(f'Ошибка. Допустимое количество сторон {self.sides_count},'
                  f' внесено {len(new_sides)}')
            return
        self.__sides = [*new_sides]


class Circle(Figure):
    sides_count = 1

    def __init__(self, colors: tuple, *sides_qty: int, filled=False):
        super().__init__(colors, *sides_qty, filled=filled)
        self.__radius = (self.get_sides()[0] / (2 * 3.14))

    def get_square(self):
        return self.get_sides()[0] ** 2 / (4 * 3.14)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = 0.5 * (self.__sides[0] + self.__sides[1] + self.__sides[2])
        return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, colors: tuple, *sides_qty: int, filled=False):
        super().__init__(colors, *sides_qty, filled=filled)
        self.set_sides(*[sides_qty[0] for _ in range(0, self.sides_count)])

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


