def sqrt(n):
    return n ** 0.5

def external_func():
    return 23

def _internal_func():
    return 45

if __name__ == '__main__':
    a = sqrt(4)
    print(a == 2)
