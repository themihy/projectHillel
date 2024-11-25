class Student:
    def __init__(self, gender, age, first_name, last_name, id_number):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        return hash(str(self))  # Нужно для использования в колекціях, которые требуют хешування