
from src.models.models import Employee, Customer


def orders_creation(new_customers, regular_customers):
    pass


def complaints_creation():
    pass


def emulation(workshop, employees, day):
    employee_turnover(employees)
    number_of_new_customers = 1
    new_customers = [Customer(day) for _ in range(number_of_new_customers)]
    number_of_regular_customers = 0  # TODO regular customers
    regular_customers = []
    orders_creation(new_customers, regular_customers)
    complaints_creation()


def employee_turnover(day, employees_list):
    for employee in employees_list:  # employees turnover function
        if not employee.quit_date:
            if employee.quits(day.strftime('%d/%m/%Y')):
                employees_list.append(Employee(hire_date=day.strftime('%d/%m/%Y'),
                                               salary=employee.salary,
                                               position=employee.position,
                                               facility=employee.facility))
