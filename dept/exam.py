class Exam:
    def __init__(self, name, passMark, subject):
        self.name = name
        self.passMark = passMark
        self.subject = subject
        

    def log(self):
        print(self.__dict__)

    def __str__(self):
        ads = self.address.__str__()
        return f'Name:{self.name}, Pass Mark:{self.passMark}, Subject:{self.subject}'


    