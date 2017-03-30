def while_elif_break():

    tries = 0
    answer = "Watson"
    while (tries <= 3):
        print("What is the name of the computer that played on Jeopardy")
        response = input()
        tries = tries + 1
        if (response == "Watson"):
            print("That is correct")
            break
        elif (tries == 3):
            print("Sorry, the answer is Watson")
            break
        else:
            print("Sorry, Try again")

if __name__ == "__main__":
        while_elif_break()