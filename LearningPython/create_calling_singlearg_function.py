def square(number):
    return number * number 


def numVowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if string[i] == "a" or string[i] == "e" or \
           string[i] == "i" or string[i] == "o" or \
           string[i] == "u":
            count = count + 1
    return count

if __name__ == "__main__":
    print("Enter a number:")
    num = int(input())
    numbersquared = square(num)
    print(str(num) + " Squared = " + str(numbersquared))

if __name__ == "__main__":
    print("Enter a string:")
    strng = str(input())
    print("There are " + str(numVowels(strng)) + " in the string")
