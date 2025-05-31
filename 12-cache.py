import time
from functools import lru_cache

@lru_cache(maxsize=3)
def steps_to(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return (
            steps_to(n - 1) +
            steps_to(n - 2) +
            steps_to(n - 3)
        )

t0 = time.perf_counter()
print(steps_to(5))
t1 = time.perf_counter()
print(t1 - t0)
print(steps_to.cache_info())