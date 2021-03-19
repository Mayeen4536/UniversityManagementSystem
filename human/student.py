from .uniperson import Uniperson

class Student(Uniperson):
    def __init__(self, id, name, studentID, guardian):
        super().__init__(id, name)
        self.studentID = studentID
        self.guardian = guardian
        self.exams =[]
        self.fee = 0


    def __str__(self):
        ptm = super().__str__()
        return f'{ptm}, StudentID:{self.studentID}, Guardian:{self.guardian}'