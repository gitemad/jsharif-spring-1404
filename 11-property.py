# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
    
#     def get_x(self):
#         return self._x
    
#     def set_x(self, value):
#         self._x = value
    
#     def get_y(self):
#         return self._y
    
#     def set_y(self, value):
#         self._y = value
    
# p = Point(1, 1)

# print(p.get_x())

# p.set_x(2)
# print(p.get_x())


# class Circle:
#     def __init__(self, radius):
#         self._set_radius(radius)
    
#     def _get_radius(self):
#         print('get radius')
#         return self._radius
    
#     def _set_radius(self, value):
#         print('set radius')
#         if value <= 0:
#             raise Exception('Radius must be a positive number')
#         self._radius = value
    
#     radius = property(
#         fget=_get_radius,
#         fset=_set_radius,
#         doc='The radius of circle'
#     )

# c = Circle(2)

# print(c.radius)
# c.radius = 5

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
    
#     @property
#     def radius(self):
#         """The radius of circle"""
#         print('get radius')
#         return self._radius
    
#     @radius.setter
#     def radius(self, value):
#         print('set radius')
#         if value <= 0:
#             raise ValueError('The radius must be a positive number')
#         self._radius = value
    
#     @radius.deleter
#     def radius(self):
#         print('delete radius')
#         del self._radius

# c = Circle(2)

# print(c.radius)
# c.radius = 5
# print(c.radius)

# # read-only attribute
# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
    
#     @property
#     def x(self):
#         return self._x
    
#     @property
#     def y(self):
#         return self._y

# p = Point(2, 1)
# print(p.x)

# p.x = 5
# print(p.x)

# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
    
#     @property
#     def area(self):
#         return self.width * self.length

# r = Rectangle(2, 4)
# print(r.area)

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @classmethod
    def unit_circle(cls):
        return cls(1)
    
    @staticmethod
    def pi():
        return 3.141592

c = Circle.unit_circle()
print(c.radius)
print(Circle.pi())
print(c.pi())