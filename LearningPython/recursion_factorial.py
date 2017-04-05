def fact(number):

    if number <= 1:
        return 1
    else:
        return number * fact(number - 1)


def explode(word):

    if len(word) <= 1:
        return word
    else:
        return word[0] + ' ' + explode(word[1:])


if __name__ == "__main__":
    print(fact(10))


def explode_main():

    print("Enter the word")
    strng = input()
    print(explode(strng))


if __name__ == "__main__":
    explode_main()





