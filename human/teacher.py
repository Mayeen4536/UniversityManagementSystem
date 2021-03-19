from .employee import Employee

class Teacher(Employee):
    def __init__(self, id, name, employeeID, salary, subject):
        super().__init__(id, name, employeeID, salary)
        self.subject = subject
       


    def __str__(self):
        ptm = super().__str__()
        return f'{ptm}, Subject:{self.subject}'