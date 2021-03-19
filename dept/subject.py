class Subject:
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit
        
        

    def log(self):
        print(self.__dict__)

    def __str__(self):
        ads = self.address.__str__()
        return f'Name:{self.name}, Credit:{self.credit}'


    