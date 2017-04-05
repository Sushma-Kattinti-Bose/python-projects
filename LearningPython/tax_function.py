def tax(amount):
 
    if amount <= 240:
        return 0
    elif amount > 240 and amount <= 480:
        return amount * .15
    else:
        return amount * .28


def netpay(grosspay):
    return grosspay - tax(grosspay)


def main():
    print("Enter the gross pay: ")
    gp = int(input())
    print("Net Pay is " + str(netpay(gp)))

if __name__ == "__main__":
    main()
