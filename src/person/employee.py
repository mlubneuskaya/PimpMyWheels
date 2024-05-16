import random

from .person import Person


class Employee(Person):
    def __init__(self, position, salary, facility, hire_date):
        super().__init__("pimpmywheels")
        self.salary = salary
        self.position = position
        self.facility = facility
        self.hire_date = hire_date
        self.quit_date = None

    def quits(self, date):
        if random.random() < 1 / (260 * 3):
            self.quit_date = date
            return True
        return False
