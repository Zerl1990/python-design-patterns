import abc


class Employee(abc.ABC):

    @abc.abstractmethod
    def show_details(self, indent_char="\t", indent=0):
        pass
