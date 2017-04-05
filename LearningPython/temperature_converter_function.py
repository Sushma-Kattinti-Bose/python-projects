def ftoc(temp):
    return (temp - 32.0) * (5.0 / 9.0)


def ctof(temp):
    return temp * (9.0 / 5.0) + 32.0


def converter(temp, toscale):
    if toscale.upper() == "C":
        return ftoc(temp)
    else:
        return ctof(temp)


def main():
    print("Enter the temperature:")
    temp = int(input())
    print("Enter the toScale in Uppercase: ")
    scale = str(input())
    converttemp = converter(temp, scale)
    print(temp, converttemp, scale)

if __name__ == "__main__":
    main()
