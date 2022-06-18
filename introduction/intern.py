from introduction.employee import Employee


class Intern(Employee):

    def __init__(self, first_name: str, last_name: str, salary: float):
        super().__init__(first_name, last_name, salary)
        self.salary = salary  # Cap salary

    @Employee.salary.setter
    def salary(self, value):
        if value > 500:
            self._salary = 500
        else:
            self._salary = value


if __name__ == '__main__':
    full = Employee('Employee', 'One', 1000)
    intern = Intern('Intern', 'One', 300)
    for tmp in [full, intern]:
        tmp: Employee
        tmp.salary = 100000
        print(f'New salary for {tmp.first_name} {tmp.last_name} is {tmp.salary}')

