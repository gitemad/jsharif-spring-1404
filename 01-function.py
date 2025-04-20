# # positional argument or required argument
# def print_bill_item(item, cost):
#     print(f'{item}: {cost}$')

# print_bill_item('Mobile', 1500)
# print_bill_item(1500, 'Mobile')
# # print_bill_item('Mobile')
# print_bill_item('Mobile', 1500, 2)

# # keyword argument
# def print_bill_item(item, fee, num):
#     print(f'item: {item}\t fee: {fee}$\t cost: {fee * num}$')

# print_bill_item(num=2, fee=10, item='Cheese')
# print_bill_item('Cheese', 10, 2)
# print_bill_item('Cheese', num=2, fee=10)
# print_bill_item(item='Cheese', 10, 2)

# # default parameter
# def print_bill_item(item, fee, num=1):
#     print(f'item: {item}\t fee: {fee}$\t cost: {fee * num}$')

# print_bill_item('Cheese', 10)
# print_bill_item('Cheese', 10, 2)
# print_bill_item('Cheese', 10, num=2)

# def f(my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append('###')
#     return my_list

# print(f(my_list=[1, 2, 3]))
# print(f(my_list=['a', 'b', 'c']))
# print(f())

# print(f())
# print(f())
# print(f(my_list=[1, 2, 3]))
# print(f())

# def f(s_in):
#     print('inside', s_in, id(s_in))
#     s_in += '12'
#     print('inside', s_in, id(s_in))

# s_out = 'abc'
# print('outside', s_out, id(s_out))
# f(s_out)
# print('outside', s_out, id(s_out))

# def f(lst_in):
#     print('inside', lst_in, id(lst_in))
#     lst_in += ['12']
#     print('inside', lst_in, id(lst_in))

# lst_out = ['abc']
# print('outside', lst_out, id(lst_out))
# f(lst_out)
# print('outside', lst_out, id(lst_out))

# def sqrt(n):
#     return n ** 0.5

# def f():
#     return 1, 2, 3

# def avg(*nums):
#     total = 0
#     for num in nums:
#         total += num
    
#     return total / len(nums)

# print(avg(1))
# print(avg(1, 2))
# print(avg(1, 2, 3))
# print(avg(1, 2, 3, 4))

# def f(x, y, z):
#     print(f'x: {x}')
#     print(f'y: {y}')
#     print(f'z: {z}')

# t = (1, 2, 3)
# f(*t)

# def f(**kwargs):
#     for key, val in kwargs.items():
#         print(f'{key}-> {val}')

# f(a=1, b=2, c=3)

# # keyword-only argument
# def concat(*dirs, prefix='$'):
#     '''concat dirs with /'''
#     print(f'{prefix} {"/".join(dirs)}')

# concat('programming', 'python', 'django', 'jsharif')
# concat('programming', 'python', 'django', 'jsharif', prefix='#')

# sqrt = lambda n: n ** 0.5

# print(list(map(sqrt, [1, 2, 3, 4])))

# def f(a: int, b: str) -> str:
#     pass

def area(r: float) -> float:
    'calculate area of circle'
    return 3.141592 * (r ** 2)
