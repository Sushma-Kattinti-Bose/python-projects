def guessing_game():

    answer = "Watson"
    print("Let's play guessing game, you have only three chances")
    print("What is the name of the computer that played on Jeopardy")
    # Get input from the user
    response = input()
    # Nested if else statements
    if response == answer:
        print("That is correct!")
    else:
        print("Sorry, Please guess again: ")
        response = input()
        if response == answer:
            print("That is correct!")
        else:
            print("Sorry, please guess one more time: ")
            response = input()
            if response == answer:
                print("That is correct!")
            else:
                print("Sorry, The correct answer is:" + answer + '.')

if __name__ == "__main__":
    guessing_game()
