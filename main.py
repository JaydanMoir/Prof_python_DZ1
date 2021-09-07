from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

name_employee = "Василий"
salary = 35000

if __name__ == '__main__':
    print(calculate_salary(name_employee, salary))
    print(get_employees(name_employee))
    print(datetime.now().replace(microsecond=0))