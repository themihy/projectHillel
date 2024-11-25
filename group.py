class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise ValueError("Cannot add more than 10 students.")
        self.students.append(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)

    def __str__(self):
        return f"Group {self.group_name}: {', '.join(str(s) for s in self.students)}"