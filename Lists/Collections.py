def getLetterGrade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")
grade1 = float(input("Enter grade: "))
grade2 = float(input("Enter grade: "))
grade3 = float(input("Enter grade: "))
grade4 = float(input("Enter grade: "))
grade5 = float(input("Enter grade: "))

average = (grade1 + grade2 + grade3 + grade4 + grade5) / 5
letterGrade = getLetterGrade(average)

print()
print(name)
print()
print("Average:", average)
print()
print("Letter Grade:", letterGrade)