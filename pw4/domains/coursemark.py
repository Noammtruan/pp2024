import math

class CourseMark:
    def __init__(self):
        self.StudentMarks = {}

    def add_mark(self, CourseID, StudentID, Mark):
        if CourseID not in self.StudentMarks:
            self.StudentMarks[CourseID] = {}
        self.StudentMarks[CourseID][StudentID] = math.floor(Mark * 10) / 10

    def get_mark(self, CourseID, StudentID):
        return self.StudentMarks.get(CourseID, {}).get(StudentID, "")

    def mark_information(self, CourseID, Students):
        if CourseID not in self.StudentMarks:
            return "Empty"

        result = []
        for student in Students:
            mark = self.get_mark(CourseID, student.StudentID)
            result.append(f"{student.StudentName} (ID: {student.StudentID}): {mark:.1f}")
        return "\n".join(result)
