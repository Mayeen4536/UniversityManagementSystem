from .employee import Employee

class Staff(Employee):
    def __init__(self, id, name, employeeID, salary, title):
        super().__init__(id, name, employeeID, salary)
        self.title = title
       


    def __str__(self):
        ptm = super().__str__()
        return f'{ptm}, Subject:{self.title}'