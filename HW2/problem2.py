import copy
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        self.color = 'black'
        self.area = 0

    @abstractmethod
    def draw(self):
        pass

    def clone(self, **kwargs):
        cloned_shape = copy.deepcopy(self)
        cloned_shape.__dict__.update(kwargs)
        return cloned_shape

    def __str__(self):
        return f'A {self.__class__.__name__} with color {self.color} and area {self.area}'


class Circle(Shape, object):

    def draw(self):
        print("Circle draw call")


class Square(Shape):

    def draw(self):
        print("Square draw call")


class Rectangle(Shape):

    def draw(self):
        print("Rectangle draw call")


class ShapeCache:
    def __init__(self):
        self.all_shapes = {cls.__name__: cls for cls in Shape.__subclasses__()}
        self.__cache = {name: None for name in self.all_shapes}

    def get_shape(self, shape):
        if shape not in self.all_shapes:
            raise ValueError(f"{shape} is not supported!")
        if self.__cache[shape]:
            return self.__cache[shape]
        else:
            return self.all_shapes[shape]()


def __main__():
    shape_cache = ShapeCache()
    circle = shape_cache.get_shape('Circle').clone(color='red', area=5)
    print(circle)



if __name__ == "__main__":
    __main__()
