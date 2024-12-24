import math
import numpy as np
import curses

class Students:
    def __init__(self, StudentName, StudentID, StudentDoB):
        self.StudentName = StudentName
        self.StudentID = StudentID
        self.StudentDoB = StudentDoB
        self.GPA = 0

    def Information(self):
        return f"Name: {self.StudentName}, ID: {self.StudentID}, DoB: {self.StudentDoB}, GPA: {self.GPA:.2f}"

class Courses:
    def __init__(self, CourseName, CourseID, Credits):
        self.CourseName = CourseName
        self.CourseID = CourseID
        self.Credits = Credits

    def Information(self):
        return f"Course Name: {self.CourseName}, Course ID: {self.CourseID}, Credits: {self.Credits}"

class CourseMark:
    def __init__(self):
        self.StudentMarks = {}

    def AddMark(self, CourseID, StudentID, Mark):
        if CourseID not in self.StudentMarks:
            self.StudentMarks[CourseID] = {}
        self.StudentMarks[CourseID][StudentID] = math.floor(Mark * 10) / 10

    def GetMark(self, CourseID, StudentID):
        return self.StudentMarks.get(CourseID, {}).get(StudentID, "")

    def MarkInformation(self, CourseID, Students):
        if CourseID not in self.StudentMarks:
            return "Empty"

        result = []
        for student in Students:
            mark = self.GetMark(CourseID, student.StudentID)
            result.append(f"{student.StudentName} (ID: {student.StudentID}): {mark:.1f}")
        return "\n".join(result)

class Manager:
    def __init__(self):
        self.Students = []
        self.Courses = []
        self.CourseMark = CourseMark()

    def InputStudentInformation(self):
        NumberStudents = int(input("Enter number of students: "))
        for _ in range(NumberStudents):
            StudentName = input("Enter name of student: ")
            StudentID = input("Enter student ID: ")
            StudentDoB = input("Enter the DoB of Student (DD/MM/YY): ")
            self.Students.append(Students(StudentName, StudentID, StudentDoB))

    def InputCourseInformation(self):
        NumberCourses = int(input("Enter number of courses: "))
        for _ in range(NumberCourses):
            CourseName = input("Enter name of course: ")
            CourseID = input("Enter course ID: ")
            Credits = int(input("Enter course credits: "))
            self.Courses.append(Courses(CourseName, CourseID, Credits))

    def InputMarkInformation(self):
        print("\nCourses:")
        for index, course in enumerate(self.Courses, 1):
            print(f"{index}. {course.CourseName} (ID: {course.CourseID})")

        CourseIndex = int(input("Select Number: ")) - 1
        if CourseIndex < 0 or CourseIndex >= len(self.Courses):
            print("Invalid course")
            return

        SelectedCourseID = self.Courses[CourseIndex].CourseID
        for student in self.Students:
            Mark = float(input(f"Enter mark for {student.StudentName} (ID: {student.StudentID}): "))
            self.CourseMark.AddMark(SelectedCourseID, student.StudentID, Mark)

    def CalculateGPA(self):
        for student in self.Students:
            total_credits = 0
            weighted_sum = 0
            for course in self.Courses:
                mark = self.CourseMark.GetMark(course.CourseID, student.StudentID)
                if mark != "":
                    total_credits += course.Credits
                    weighted_sum += mark * course.Credits
            student.GPA = weighted_sum / total_credits if total_credits > 0 else 0

    def SortStudentsByGPA(self):
        self.Students.sort(key=lambda student: student.GPA, reverse=True)

    def DisplayStudents(self):
        return "\n".join(student.Information() for student in self.Students)

    def DisplayCourses(self):
        return "\n".join(course.Information() for course in self.Courses)

    def DisplayMarks(self):
        print("\nCourses:")
        for index, course in enumerate(self.Courses, 1):
            print(f"{index}. {course.CourseName} (ID: {course.CourseID})")

        CourseID = input("Enter Course ID: ")
        course_found = any(course.CourseID == CourseID for course in self.Courses)

        if not course_found:
            print("Invalid ID")
        else:
            print("\nMarks:")
            print(self.CourseMark.MarkInformation(CourseID, self.Students))

    def CursesUI(self, stdscr):
        curses.curs_set(0)
        stdscr.clear()
        menu = ["1. Input Student Information", "2. Input Course Information", "3. Input Mark Information", "4. Display Students", "5. Display Courses", "6. Display Marks", "7. Calculate GPA", "8. Sort Students by GPA", "9. Exit"]
        current_row = 0

        while True:
            stdscr.clear()
            for idx, row in enumerate(menu):
                if idx == current_row:
                    stdscr.addstr(idx, 0, row, curses.color_pair(1))
                else:
                    stdscr.addstr(idx, 0, row)

            key = stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
                current_row += 1
            elif key == ord("\n"):
                if current_row == 0:
                    self.InputStudentInformation()
                elif current_row == 1:
                    self.InputCourseInformation()
                elif current_row == 2:
                    self.InputMarkInformation()
                elif current_row == 3:
                    stdscr.addstr(len(menu) + 2, 0, self.DisplayStudents())
                    stdscr.getch()
                elif current_row == 4:
                    stdscr.addstr(len(menu) + 2, 0, self.DisplayCourses())
                    stdscr.getch()
                elif current_row == 5:
                    self.DisplayMarks()
                elif current_row == 6:
                    self.CalculateGPA()
                elif current_row == 7:
                    self.SortStudentsByGPA()
                elif current_row == 8:
                    break

            stdscr.refresh()

def main():
    manager = Manager()
    curses.wrapper(manager.CursesUI)

if __name__ == "__main__":
    main()
