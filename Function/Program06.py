# generator function


def my_generator():             
    yield 1
    yield 2
    yield 3

values = my_generator()

print(next(values))
print(next(values))
print(next(values))


        