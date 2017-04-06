def square(number):
    return number * number

num = 2
sqnum = square(num)
sqnumber = square
sqnum = sqnumber(2)
print(sqnum)

numbers = [1, 2, 3, 4]
numbersq = list(map(square, numbers))
print(numbersq)

if __name__ == "__main__":
    square(2)

