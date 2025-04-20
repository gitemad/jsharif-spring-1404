class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __pos__(self):
        return Point(self.x, self.y)
    
    def __eq__(self, other: 'Point'):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
    
    def __neg__(self):
        return Point(-self.x, -self.y)
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __add__(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y)
    
    # in-place addition
    def __iadd__(self, other: 'Point'):
        self.x += other.x
        self.y += other.y
        return self

p1 = Point(4, 3)
p2 = +p1
p3 = -p1

# __del__(self)

# __invert__(self) # ~obj
# __round__(self) # round(obj)
# __floor__(self) # floor(obj)
# __ceil__(self) # ceil(obj)

# __sub__(self, other) # obj - other
# __mul__(self, other) # obj * other
# __floordiv__(self, other) # obj // other
# __truediv__(self, other) # obj / other
# __mod__(self, other) # obj % other
# __pow__(self, other) # obj ** other
# __lshift__(self, other) # obj << other
# __rshift__(self, other) # obj >> other
# __and__(self, other) # obj & other
# __or__(self, other) # obj | other
# __xor__(self, other) # obj ^ other

# __isub__(self, other) # obj -= other
# __imul__(self, other) # obj *= other
# __ifloordiv__(self, other) # obj //= other
# __itruediv__(self, other) # obj /= other
# __imod__(self, other) # obj %= other
# __ipow__(self, other) # obj **= other
# __ilshift__(self, other) # obj <<= other
# __irshift__(self, other) # obj >>= other
# __iand__(self, other) # obj &= other
# __ior__(self, other) # obj |= other
# __ixor__(self, other) # obj ^= other

# __lt__(self, other) # obj < other
# __le__(self, other) # obj <= other
# __gt__(self, other) # obj > other
# __ge__(self, other) # obj >= other
# __eq__(self, other) # obj == other
# __ne__(self, other) # obj != other

# __int__(self) # int(obj)
# __float__(self) # float(obj)
# __bool__(self) # bool(obj)
# __complex__(self) # complex(obj)
# __oct__(self) # oct(obj)
# __hex__(self) # hex(obj)
# __str__(self) # str(obj)

# __len__ # len(obj)