class Address:
    def __init__(self, roadNo, city, region, country, postalCode):
        self.roadNo = roadNo
        self.city = city
        self.region = region
        self.country = country
        self.postalCode = postalCode

    def log(self):
        print(self.__dict__)

    def __str__(self):
        return f'Road No.:{self.roadNo}, City:{self.city}, Region:{self.region}, Country: {self.country}, Postal Code: {self.postalCode}'

