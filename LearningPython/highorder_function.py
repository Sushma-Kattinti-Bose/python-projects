import functools


def square(number):
    return number * number


def even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def sum(x, y):
    return x + y


numbers = [1, 2, 3]
print(numbers)
numbersq = list(map(square, numbers))
print(numbersq)

numbers = list(range(1, 11))
evens = list(filter(even, numbers))
print(evens)

numbers = list(range(1, 11))
sum = functools.reduce(sum, numbers)
print("The sum of the range is" + ' ' + str(sum))


