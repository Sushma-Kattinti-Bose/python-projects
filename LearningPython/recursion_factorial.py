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


def explode_main():

    print("Enter the word")
    strng = input()
    print(explode(strng))


def remove_duplicates(word):

    if len(word) <= 1:
        return word
    elif word[0] == word[1]:
        return remove_duplicates(word[1:])
    else:
        return word[0] + remove_duplicates(word[1:])


def remove_duplicates_main():

    print("Enter the sentence")
    sentence = str(input())
    print(remove_duplicates(sentence))
    
if __name__ == "__main__":
    print(fact(10))


if __name__ == "__main__":
    explode_main()

if __name__ == "__main__":
    remove_duplicates_main()



