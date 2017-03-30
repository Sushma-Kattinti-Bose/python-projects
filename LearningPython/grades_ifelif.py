def grades_ifelif():

    print("Enter a numeric grade:")
    grade = int(input())
    if grade >= 90:
        letterGrade = "A"
    elif grade >= 80:
        letterGrade = "B"
    elif grade >= 70: 
        letterGrade = "C"
    elif grade >= 60:
        letterGrade = "D"
    elif grade <= 59: 
        letterGrade = "F"
    else:
        print("Did not recognise input")
    print("Your Grade is: " + letterGrade)

if __name__ == "__main__":
    grades_ifelif()
