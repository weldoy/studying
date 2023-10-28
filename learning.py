def how_iter_works():
    numbers = [1, 2, 3, 4, 5]
    i = iter(numbers)

    while True:
        try:
            item = next(i)
            ...
        except StopIteration:
            break


def iterators():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_string = 'I like Python'

    squares = map(lambda num: num ** 2, numbers)
    capitals = map(str.upper, my_string)

    print(*squares, sep=' ')
    print(*capitals, sep=' ')
