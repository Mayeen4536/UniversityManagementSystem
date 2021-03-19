

class Person():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.blood = ''
        self.contact = None
        pass

    def log(self):
        print(self.__dict__)

    def __str__(self):
        return f'ID:{self.id}, Name:{self.name}'

