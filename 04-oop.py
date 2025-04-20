from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color='black'):
        self.color = color
    
    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Shape):
    sides_count = 4

    def __init__(self, width, length, color='black'):
        super().__init__(color)
        # super(Rectangle, self).__init__(color)

        self.width = width
        self.length = length
    
    def get_area(self):
        return self.width * self.length

class Square(Rectangle):
    def __init__(self, width, color='black'):
        super().__init__(width, width, color)

class Circle(Shape):
    def __init__(self, radius, color='black'):
        super().__init__(color)
        self.radius = radius
    
    # override
    def get_area(self):
        return 3.14 * (self.radius ** 2)

rect1 = Rectangle(3, 4, 'blue')
rect2 = Rectangle(5, 5)

square1 = Square(4)
circle1 = Circle(2, 'red')
print(circle1.get_area())
print(circle1.color)

# class A:
#     def __init__(self):
#         super().__init__()
#         print('A')

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print('B')

# class C(A):
#     def __init__(self):
#         super().__init__()
#         print('C')

# class D(A):
#     def __init__(self):
#         super().__init__()
#         print('D')

# class E(D, C, B):
#     def __init__(self):
#         super().__init__()
#         print('E')

# E()