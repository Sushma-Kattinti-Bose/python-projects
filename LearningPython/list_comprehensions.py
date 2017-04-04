def list_comprehensions():

    grades = [76, 89, 90, 66]
    print(grades)
    grades = [grade + 5 for grade in grades]
    print(grades)
    words = ["NOW", "IS", "THE", "TIME"]
    print(words)
    words = [word.lower() for word in words]
    print(words)

if __name__ == "__main__":
    list_comprehensions()