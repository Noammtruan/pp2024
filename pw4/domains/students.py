class Students:
    def __init__(self, StudentName, StudentID, StudentDoB):
        self.StudentName = StudentName
        self.StudentID = StudentID
        self.StudentDoB = StudentDoB
        self.GPA = 0

    def information(self):
        return f"Name: {self.StudentName}, ID: {self.StudentID}, DoB: {self.StudentDoB}, GPA: {self.GPA:.2f}"
