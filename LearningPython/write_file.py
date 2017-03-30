def write_file():
    outFile = open("grades.txt", 'w')
    grade = 0
    print("Enter the grade, (q) to quit: ")
    grade = input()
    while (grade != 'q'):
        outFile.write(grade + '\n')
        print("Enter the grade, (q) to quit: ")
        grade = input()
    outFile.close()

if __name__ == "__main__":
    write_file()
