from introduction.employee import Employee


class TempEmployee(Employee):

    def __init__(self, first_name: str, last_name: str, salary: float):
        super().__init__(first_name, last_name, salary)
        self.salary = salary  # Cap salary

    @Employee.salary.setter
    def salary(self, value):
        if value > 1000:
            self._salary = 1000
        else:
            self._salary = value
