from .person import Person

class Guardian(Person):
    def __init__(self, id, name, profession, income):
        super().__init__(id, name)
        self.profession = profession
        self.income = income


    def __str__(self):
        ptm = super().__str__()
        return f'{ptm}, Profession:{self.profession}, Income:{self.income}'