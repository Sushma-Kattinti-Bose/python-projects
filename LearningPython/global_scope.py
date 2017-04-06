# def getNumber():
#     "Make a call to the number from inside the function"
#     print(number)


def test_scope(value):
    value = 4
    print(value)

value = 2
test_scope(value)
print(value)

# number = 1
# print(number)
# getNumber()