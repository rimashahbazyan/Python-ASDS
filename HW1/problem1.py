from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Circle draw call")


class Square(Shape):
    def draw(self):
        print("Square draw call")


class Triangle(Shape):
    def draw(self):
        print("Triangle draw call")


class ShapeFactory:
    def __init__(self):
        self.all_shapes = {cls.__name__: cls for cls in Shape.__subclasses__()}

    def validate_shape_name(self, shape_name):
        if shape_name not in self.all_shapes:
            raise ValueError(f'Shape "{shape_name}" does not exist!')

    def get_shape(self, shape_name) -> Shape:
        self.validate_shape_name(shape_name)
        shape_class = self.all_shapes[shape_name]
        return shape_class()


class Client:
    def draw_object(self):
        shape_name = input("What shape do you want to draw? ").capitalize()
        shape_factory = ShapeFactory()
        shape = shape_factory.get_shape(shape_name)
        shape.draw()


if __name__ == "__main__":
    client = Client()
    client.draw_object()
