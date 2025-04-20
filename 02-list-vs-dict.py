import time
import sys

start = time.perf_counter()
lst = [i for i in range(20_000_000)]
end = time.perf_counter()
print(f'list: {end - start}')

start = time.perf_counter()
dct = {i: i for i in range(20_000_000)}
end = time.perf_counter()
print(f'dict: {end - start}')

start = time.perf_counter()
print(19_999_999 in lst)
end = time.perf_counter()

list_time = end - start
print(f'list: {list_time}')

start = time.perf_counter()
print(19_999_999 in dct)
end = time.perf_counter()

dict_time = end - start
print(f'dict: {dict_time}')

print(f'list / dict: {list_time / dict_time}')

print(sys.getsizeof(lst))
print(sys.getsizeof(dct))

start = time.perf_counter()
lst2 = []
for i in range(20_000_000):
    lst2.append(i)
end = time.perf_counter()
print(end - start)