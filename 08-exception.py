# age = int(input('Enter your age: '))

# if age < 0:
#     raise Exception(f'Age must be positive. The value of age was {age}')

# num = int(input('Enter numerator:'))
# den = int(input('Enter denominator:'))
# d = {
#     'name': 'Emad'
# }
# l = [1, 2, 3]

# try:
#     print(l[4])
#     print(d['age'])
#     print(num / den)
# except ZeroDivisionError:
#     print('Denominator must not be zero')
# except (KeyError, IndexError) as e:
#     print(e)
# except:
#     print('Unknown error')

# print('end')

# l = [1, 2, 3]

# try:
#     print(l[5])
# except Exception as e:
#     print(e)
# else:
#     print('Executing else caluse')
# finally:
#     print('executing finally clause')

class CustomError(Exception):
    def __init__(self, arg1, msg='', *args):
        super().__init__(*args)
