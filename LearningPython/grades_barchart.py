def grades_barchart():

    bar = ""
    for grade in open('grades.txt'):
        for i in range(1, int(grade)+1):
            if i % 5 == 0:
                bar = bar + "*"
        print(bar, i)
        bar = ""

if __name__ == "__main__":
    grades_barchart()