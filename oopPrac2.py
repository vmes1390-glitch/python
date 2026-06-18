class Student:
    def __init__(self, name, student_id, grades = None):
        self.__name  = name
        self.__student_id = student_id
        self.__grades = []
        self.grades = grades if grades else []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def student_id(self):
        return self.__student_id
    
    @student_id.setter
    def student_id(self, student_id):
        self.__student_id = student_id

    @property
    def grades(self):
        return self.__grades.copy()
    
    @grades.setter
    def grades(self, grades):
        if not isinstance(grades, list):
            raise ValueError("input a list as grades!")
        
        for grade in grades:
            if not isinstance(grade, (int, float)):
                raise ValueError("grade(s) shoud be int or float!")
            
            if not 0 <= grade <= 20:
                raise ValueError("grade shoud be between 0 and 20!")
            
        self.__grades = grades.copy()

    def add_grade(self, newGrades):
                
        for grade in newGrades:
            if not isinstance(grade, (int, float)):
                raise ValueError("grade(s) shoud be int or float!")
            
            if not 0 <= grade <= 20:
                raise ValueError("grade shoud be between 0 and 20!")
            
        self.__grades.extend(newGrades)

    def mean(self):
        if not self.__grades:
            return 0

        return sum(self.__grades) / len(self.__grades)
    
    def __str__(self):
        return f"name: {self.__name}, id: {self.__student_id}, grades: {self.__grades}, mean: {self.mean()}"
    

std = Student("Erfan Lotfi", 14034422003, [20, 10])
std.add_grade([12, 15])

print(std)
