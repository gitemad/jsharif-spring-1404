# single leading underscore (_var)
# import sample_module
# # from sample_module import _internal_func
# from sample_module import *

# print(sample_module._internal_func())
# print(_internal_func())

# # single trailing underscore (var_)
# def make_object(name, class_):
#     pass

# # double leading underscore (__var)
# class Test:
#     def __init__(self):
#         self.a = 1
#         self._b = 2
#         self.__c = 3

# class ExtendedTest(Test):
#     def __init__(self):
#         super().__init__()
#         self.a = 'overridden'
#         self._b = 'overridden'
#         self.__c = 'overridden'

# t = ExtendedTest()
# print(t.a)
# print(t._b)
# print(t._Test__c)
# print(t._ExtendedTest__c)

# double leading and trailing underscore (__var__)
class A:
    def __init__(self):
        pass

# single underscore
for _ in range(5):
    print('Hello')

name, creator, _ = ('Python', 'Guido Van Rossum', 1991)

3_000_000_000