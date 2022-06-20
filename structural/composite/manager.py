from structural.composite.employee import Employee


class Manager(Employee):

    def __init__(self, first_name: str, last_name: str, salary: int):
        self._fname = first_name
        self._lname = last_name
        self._salary = salary
        self._subordinates = []

    def add_employee(self, employee: Employee):
        self._subordinates.append(employee)

    def remove_employee(self, employee: Employee):
        self._subordinates.remove(employee)

    def show_details(self, indent_char="\t", indent=0):
        print(f"{indent_char * indent}First Name: {self._fname}, Last Name: {self._lname},  Salary: {self._salary}")
        for subordinate in self._subordinates:
            subordinate: Employee
            subordinate.show_details(indent_char, indent + 1)
