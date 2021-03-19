
class Account:
    def __init__(self, id, type, amount):
        self.id = id
        self.type = type
        self.amount = amount

    def log(self):
        print(self.__dict__)

    def __str__(self):
        return f'ID:{self.id}, Type:{self.type}, Amount:{self.amount}'

