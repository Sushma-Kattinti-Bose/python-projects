def iterator_tuples():

    square = ((10, 8), (10, 23), (25, 34), (50, 78))
    sqaureit = iter(square)
    print(next(sqaureit))
    print(next(sqaureit))
    print(next(sqaureit))
    print(next(sqaureit))


if __name__ == "__main__":
    iterator_tuples()