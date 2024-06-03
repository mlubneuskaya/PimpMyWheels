from src.models.employee import Employee


def create_employees(workshop, positions, employees_parameters, date):
    employees = [Employee(workshop, date, *employees_parameters[k].values()) for k in positions]
    return employees
