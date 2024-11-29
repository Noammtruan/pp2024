def InputStudent():
    NumberStudent = int(input("Enter number of Student: "))
    StudentsList = []
    for i in range(NumberStudent):
        StudentName = input("Enter Name of Student: ")
        StudentID = input("Enter ID of Student: ")
        StudentDoB = input("Enter DoB of Student (Ex:02/08/2005): ")
        StudentsList.append((StudentName, StudentID, StudentDoB))
    return StudentsList


def InputCourse():
    NumberCourse = int(input("Enter Number of Course: "))
    CoursesList = []
    for i in range(NumberCourse):
        CourseName = input("Enter Name of Course: ")
        CourseID = input("Enter ID of Course: ")
        CoursesList.append((CourseName, CourseID))
    return CoursesList


def InputMark(StudentsList, CoursesList, StudentMark):
    for i, course in enumerate(CoursesList, 1):
        print(f"{i} {course[0]} (ID: {course[1]})")
    CourseIndex = int(input("Select a course (by number): ")) - 1
    CourseID = CoursesList[CourseIndex][1]
    if CourseID not in StudentMark:
        StudentMark[CourseID] = {}
    for student in StudentsList:
        Mark = float(input(f"Enter mark for {student[1]} (Name: {student[0]}): "))
        StudentMark[CourseID][student[1]] = Mark
            

def displayStudent(StudentsList):
    for StudentName, StudentID, StudentDoB in StudentsList:
        print(f"Name: {StudentName}, ID: {StudentID}, DoB: {StudentDoB}")
        
def displayCourse(CoursesList):
    for CourseName, CourseID in CoursesList:
        print(f"Course: {CourseName}, ID: {CourseID}")
        
def displayMark(CourseID, StudentMark, StudentsList):
    for student in StudentsList:
        StudentName = student[0]
        StudentID = student[1]
        Mark = StudentMark[CourseID].get(StudentID, "N/A")
        print(f"{StudentName} (ID: {StudentID}): {Mark}")


def main():
    StudentsList = InputStudent()
    CoursesList = InputCourse()
    StudentMark = {}
    
    while True:
        print("1 Student")
        print("2 Course")
        print("3 Input Mark")
        print("4 Student's Mark")
        print("5 End Program")
        choice = input("Choice: ")
        if choice == "1":
            displayStudent(StudentsList)
        elif choice == "2":
            displayCourse(CoursesList)
        elif choice == "3":
            InputMark(StudentsList, CoursesList, StudentMark)
        elif choice == "4":
            for i, course in enumerate(CoursesList, 1):
                print(f"{i} {course[0]} (ID: {course[1]})")
            CourseID = input("Enter Course ID: ")
            displayMark(CourseID, StudentMark, StudentsList)
        elif choice == "5":
            print("End program.")
            break
        else:
            print("This Choice does not exist")


if __name__ == "__main__":
    main()
