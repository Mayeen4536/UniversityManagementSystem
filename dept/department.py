class Department:
    def __init__(self, name, subjects, deaan, teachers):
        self.name = name
        self.subjects = subjects
        self.dean = dean
        self.teachers = teachers
        

    def log(self):
        print(self.__dict__)

    def __str__(self):
        ads = self.address.__str__()
        return f'Name:{self.name}, Subjects:{self.subjects}, Dean:{self.dean}, Teachers:{self.teacher}'


    