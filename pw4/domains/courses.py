class Courses:
    def __init__(self, CourseName, CourseID, Credits):
        self.CourseName = CourseName
        self.CourseID = CourseID
        self.Credits = Credits

    def information(self):
        return f"Course Name: {self.CourseName}, Course ID: {self.CourseID}, Credits: {self.Credits}"
