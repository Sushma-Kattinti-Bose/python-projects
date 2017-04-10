try:
    print("Enter a numerator:")
    numer = int(input())
    print("Enter a Denominator:")
    denom = int(input())
    quotient = numer / denom
    print(quotient)
    print("Enter the filename: ")
    name = input()
    file = open(name, 'r')

except:
    print("Cannot divide by zero")
    print("Enter a Denominator:")
    denom = int(input())
    quotient = numer / denom
    print(quotient)
    print("Cannot open the file")
    print("Enter the filename: ")
    name = input()
    file = open(name, 'r')

