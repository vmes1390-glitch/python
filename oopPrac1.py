class Student:
    def __init__(self, name, student_id, grades = None):
        self.name  = name
        self.student_id = student_id
        self.grades = grades if grades else []

    def add_grade(self, newGrades):
        self.grades.extend(newGrades)

    def mean(self):
        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)
    
    def __str__(self):
        return f"name: {self.name}, id: {self.student_id}, grades: {self.grades}, mean: {self.mean()}"
    

std = Student("Erfan Lotfi", 14034422003, [20, 10])
std.add_grade([12, 15])

print(std)