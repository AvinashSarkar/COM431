class Student:
    def __init__(self, student_id, name, course, mark):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.mark = mark
        self.is_valid_mark = self.validate_mark()
        self.grade = self.determine_grade()

    def validate_mark(self):
        return 0 <= self.mark <= 100

    def determine_grade(self):
        if 0 <= self.mark <= 40:
            return "Fail"
        elif 40 <= self.mark <= 50:
            return "Third"
        elif 50 <= self.mark <= 60:
            return "Lower Second"
        elif 60 <= self.mark <= 70:
            return "Upper Second"
        elif 70 <= self.mark <= 80:
            return "First"

    def print_details(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}"
        f"Mark: {self.mark}, valid mark: {self.is_valid_mark}, grade: {self.grade}")