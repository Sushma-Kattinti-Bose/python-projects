import sys


def thankyou_note():

    print("What is the name of the gift giver")
    # input allows the user to enter the data
    name = input()
    print("What is the present they gave you")
    present = input()
    print("How old were you your birthday")
    age = int(input())
    print("What is your name?")
    yourName = input()
    print("Dear " + name + '.')
    print("Thank you for the " + present + '.')
    print("I can't believe I am already " + str(age) + " years old, but" )
    print("it does not feel much different than being " + str(age-1) + ".")
    print("Sincerly,")
    print(yourName)

if __name__ == "__main__":
    thankyou_note()