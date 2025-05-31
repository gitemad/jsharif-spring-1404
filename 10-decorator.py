# def say_hello(name):
#     return f'Hello {name}'

# def say_hi(name):
#     return f'Hi {name}'

# def greet(greeter_func, name):
#     return greeter_func(name)

# print(greet(say_hello, 'Emad'))

# def parent():
#     print('Parent')

#     def first_child():
#         print('1st child')

#     def second_child():
#         print('2nd child')
    
#     second_child()
#     return first_child

# f = parent()
# f()
# f()


# def my_decorator(func):
#     def wrapper():
#         print('before calling func')
#         func()
#         print('after calling func')
    
#     return wrapper

# @my_decorator # say_hi = my_decorator(say_hi)
# def say_hi():
#     print('Hi')

# say_hi()

# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
    
#     return wrapper

# @do_twice
# def greet(name):
#     print('calling greet')
#     return f'Hello {name}'

# print(greet('Emad'))


# def italic(func):
#     def wrapper():
#         return f'<i> {func()} </i>'
    
#     return wrapper

# def bold(func):
#     def wrapper():
#         return f'<b> {func()} </b>'
    
#     return wrapper

# @bold
# @italic
# def introcution():
#     return 'This is a basic program'

# print(introcution())

def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        
        return wrapper
    
    return decorator

@repeat(2) # greet = repeat(2)(greet)
def greet(name):
    print(f'Hello {name}')

greet('Emad')
