class Employee():
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id


    def calculate_salary(self, salary):
        return salary

    def __str__(self)-> str:
        return f"Employee {self.name} (ID: {self.employee_id})"
        


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        super().calculate_salary
        return self.hours_worked * self.hourly_rate

class Freelancer(Employee):
    def __init__(self, project_count, payment_per_project):
        self.project_count = project_count
        self.payment_per_project = payment_per_project

    def calculate_salary(self):
        super().calculate_salary
        return self.project_count * self.payment_per_project


class PayrollSystem():
    def add_employee(self, employee: Employee):
        return employee
