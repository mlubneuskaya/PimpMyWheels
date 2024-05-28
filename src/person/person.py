from .generator import get_name, get_surname, get_email, get_address, get_phone_number


class Person:

    def __init__(self, email_type='customer'):
        self.name, self.__gender = get_name()
        self.surname = get_surname(self.__gender)
        self.email = get_email(self.name, self.surname, email_type)
        self.phone_number = get_phone_number()
        self.address = get_address()
        self.birth_date = ''

    def to_list(self):
        return list(self.__dict__.values())
