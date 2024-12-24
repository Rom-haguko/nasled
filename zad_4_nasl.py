from math import pi
class Figure:
    def get_square(self):
        raise NotImplementedError("Этот метод должен быть реализован в подклассе")

    def get_volume(self):
        raise NotImplementedError("Этот метод должен быть реализован в подклассе")


class Cube(Figure):
    def __init__(self, a):
        self.a = a

    def get_square(self):
        return 6*(self.a**2)

    def get_volume(self):
        return self.a**3

    def __str__(self):
        return f'Площадь куба равна {self.get_square():.2f}, объём равен {self.get_volume():.2f}'


class Sphere(Figure):
    def __init__(self, r):
        self.r = r

    def get_square(self):
        return 4*pi*(self.r**2)

    def get_volume(self):
        return (4/3)*pi*(self.r**3)

    def __str__(self):
        return f'Площадь сферы равна {self.get_square():.2f}, объём равен {self.get_volume():.2f}'

class Cylinder(Figure):
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def get_square(self):
        return 2*pi*(self.r**2)+2*pi*self.r*self.h

    def get_volume(self):
        return pi*(self.r**2)*self.h

    def __str__(self):
        return f'Площадь цилиндра равна {self.get_square():.2f}, объём равен {self.get_volume():.2f}'

class Parallelepiped(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_square(self):
        return 2*(self.a*self.b + self.b*self.c + self.a*self.c)

    def get_volume(self):
        return self.a*self.b*self.c

    def __str__(self):
        return f'Площадь параллелепипеда равна {self.get_square():.2f}, объём равен {self.get_volume():.2f}'


class Ellipsoid(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_square(self):
        return 4*pi*((self.a*self.b+self.b*self.c*self.a*self.c)/3)**1.6

    def get_volume(self):
        return (4/3)*pi*self.a*self.b*self.c

    def __str__(self):
        return f'Площадь эллипсоида равна {self.get_square():.2f}, объём равен {self.get_volume():.2f}'



def find_dominant_shapes(figures):
    # Суммируем объёмы всех фигур
    sum_volume = sum([i.get_volume() for i in figures])
    # Выбираем фигуры, чей объём >= объёму всех остальных
    result = [i for i in figures if i.get_volume() >= (sum_volume - i.get_volume())]
    return result


list_figure = [
    Cube(10),
    Sphere(2),
    Cylinder(2, 5),
    Parallelepiped(2, 3, 4),
    Ellipsoid(2, 3, 4)
]
if find_dominant_shapes(list_figure):
    for shape in find_dominant_shapes(list_figure):
        print(shape)
else:
    print("Нет фигур, чьи объёмы равны или больше объёмов всех остальных.")


