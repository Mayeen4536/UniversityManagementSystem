from .uniperson import Uniperson

class Employee(Uniperson):
    def __init__(self, id, name, employeeID, salary):
        super().__init__(id, name)
        self.employeeID =  employeeID
        self.salary = self.salary
        


    def __str__(self):
        ptm = super().__str__()
        return f'{ptm}, EmployeeID:{self.employeeID}, Salary:{self.salary}'