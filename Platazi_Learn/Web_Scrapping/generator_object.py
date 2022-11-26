def even_numbers():
    a = 0
    yield a

    while a<100:
        a += 2
        yield a

my_gen = even_numbers()
for i in range(100):
    print(next(my_gen))
