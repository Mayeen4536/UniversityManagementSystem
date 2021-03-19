from .person import Person

class Uniperson(Person):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.department =  None
        self.account = None


    def __str__(self):
        ptm = super().__str__()
        return f'{ptm}, Department:{self.department}, Account:{self.account}'