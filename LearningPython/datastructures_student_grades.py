class Student:
    grades = []

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def addGrade(self, grade):
        self.grades.append(grade)

    def showGrades(self):
        grds = ' '
        for grade in self.grades:
            grds += str(grade) + ' '
        return grds

stu1 = Student('Beau', '123')
stu1.addGrade(81)
stu1.addGrade(99)
stu1.addGrade(87)
print(stu1.showGrades())
