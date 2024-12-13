class Students:
    def __init__(self, StudentName, StudentID, StudentDoB):
        self.StudentName = StudentName
        self.StudentID = StudentID
        self.StudentDoB = StudentDoB

    def Information(self):
        print(f"Name: {self.StudentName}, ID: {self.StudentID}, DoB: {self.StudentDoB}")


class Courses:
    def __init__(self, CourseName, CourseID):
        self.CourseName = CourseName
        self.CourseID = CourseID

    def Information(self):
        print(f"Course Name: {self.CourseName}, Course ID: {self.CourseID}")


class CourseMark:
    def __init__(self):
        self.StudentMarks = {}

    def AddMark(self, CourseID, StudentID, Mark):
        if CourseID not in self.StudentMarks:
            self.StudentMarks[CourseID] = {}
        self.StudentMarks[CourseID][StudentID] = Mark

    def GetMark(self, CourseID, StudentID):
        return self.StudentMarks.get(CourseID, {}).get(StudentID, "N/A")

    def MarkInformation(self, CourseID, Students):
        if CourseID not in self.StudentMarks:
            print("Empty Mark in Course")
            return

        for Student in Students:
            mark = self.GetMark(CourseID, Student.StudentID)
            print(f"{Student.StudentName} (ID: {Student.StudentID}): {mark}")


class Manager:
    def __init__(self):
        self.Students = []
        self.Courses = []
        self.CourseMark = CourseMark()

    def InputStudentInformation(self):
        try:
            NumberStudents = int(input("Enter number of students: "))
            for _ in range(NumberStudents):
                StudentName = input("Enter name of student: ")
                StudentID = input("Enter student ID: ")
                StudentDoB = input("Enter DoB (DD/MM/YY): ")
                self.Students.append(Students(StudentName, StudentID, StudentDoB))
        except ValueError:
            print("Invalid")

    def InputCourseInformation(self):
        try:
            NumberCourses = int(input("Enter number of courses: "))
            for _ in range(NumberCourses):
                CourseName = input("Enter name of course: ")
                CourseID = input("Enter course ID: ")
                self.Courses.append(Courses(CourseName, CourseID))
        except ValueError:
            print("Invalid")

    def InputMarkInformation(self):
        if not self.Courses:
            print("Invalid course")
            return

        print("\nCourses:")
        for index, course in enumerate(self.Courses, 1):
            print(f"{index}. {course.CourseName} (ID: {course.CourseID})")

        try:
            CourseIndex = int(input("Select a course by number: ")) - 1
            if CourseIndex < 0 or CourseIndex >= len(self.Courses):
                print("Invalid course")
                return

            SelectedCourseID = self.Courses[CourseIndex].CourseID
            for student in self.Students:
                try:
                    Mark = float(input(f"Enter mark for {student.StudentName} (ID: {student.StudentID}): "))
                    self.CourseMark.AddMark(SelectedCourseID, student.StudentID, Mark)
                except ValueError:
                    print("Invalid mark")
        except ValueError:
            print("Invalid")

    def DisplayStudents(self):
        if not self.Students:
            print("Invalid Student")
        else:
            print("\nList of Students:")
            for student in self.Students:
                student.Information()

    def DisplayCourses(self):
        if not self.Courses:
            print("Invalid Student")
        else:
            print("\nList of Courses:")
            for course in self.Courses:
                course.Information()

    def DisplayMarks(self):
        if not self.Courses:
            print("Invalid Course")
            return

        print("\nCourses:")
        for index, course in enumerate(self.Courses, 1):
            print(f"{index}. {course.CourseName} (ID: {course.CourseID})")

        CourseID = input("Enter Course ID for marks: ")
        course_found = any(course.CourseID == CourseID for course in self.Courses)

        if not course_found:
            print("Invalid Course ID")
        else:
            print("\nMarks for select course:")
            self.CourseMark.MarkInformation(CourseID, self.Students)


def main():
    manager = Manager()
    while True:
        print("\n1. Input Student Information")
        print("2. Input Course Information")
        print("3. Input Mark Information")
        print("4. Display Students")
        print("5. Display Courses")
        print("6. Display Marks")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.InputStudentInformation()
        elif choice == "2":
            manager.InputCourseInformation()
        elif choice == "3":
            manager.InputMarkInformation()
        elif choice == "4":
            manager.DisplayStudents()
        elif choice == "5":
            manager.DisplayCourses()
        elif choice == "6":
            manager.DisplayMarks()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
