class Contact:
    def __init__(self, email, phone, alternativePhone, address):
        self.email = email
        self.phone = phone
        self.alternativePhone = alternativePhone
        self.address = address

    def log(self):
        print(self.__dict__)

    def __str__(self):
        ads = self.address.__str__()
        return f'Email:{self.email}, Phone:{self.phone}, Alternate Phone:{self.alternativePhone}, {ads}'


    