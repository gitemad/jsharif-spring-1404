def odds(max):
    num = 1

    while num <= max:
        yield num
        num += 2

for i in odds(8):
    print(i)

gen = odds(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

[i for i in range(1, 8, 2)]