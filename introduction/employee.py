class Employee:

    def __init__(self, first_name: str, last_name: str, salary: float):
        self._first_name = first_name
        self._last_name = last_name
        self._salary = salary

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value


if __name__ == '__main__':
    luis = Employee("Luis", "Rivas", 1000)
    blanca = Employee("Blanca", "Moreno", 1000)
