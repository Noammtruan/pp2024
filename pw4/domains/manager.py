from .students import Students
from .courses import Courses
from .coursemark import CourseMark
from ..input import InputHandler

class Manager:
    def __init__(self):
        self.Students = []
        self.Courses = []
        self.CourseMark = CourseMark()

    def input_student_information(self):
        number_students = InputHandler.get_number("Enter number of students: ")
        for _ in range(number_students):
            student_name = InputHandler.get_string("Enter name of student: ")
            student_id = InputHandler.get_string("Enter student ID: ")
            student_dob = InputHandler.get_string("Enter the DoB of Student (DD/MM/YY): ")
            self.Students.append(Students(student_name, student_id, student_dob))

    def input_course_information(self):
        number_courses = InputHandler.get_number("Enter number of courses: ")
        for _ in range(number_courses):
            course_name = InputHandler.get_string("Enter name of course: ")
            course_id = InputHandler.get_string("Enter course ID: ")
            credits = InputHandler.get_number("Enter course credits: ")
            self.Courses.append(Courses(course_name, course_id, credits))
