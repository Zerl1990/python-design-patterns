from collections import namedtuple

Student = namedtuple("Student", ["f_name", "l_name", "identifier"])


class ClassRoomIterator:
    def __init__(self, students):
        self._students = students
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._students):
            val = self._students[self._index]
            self._index += 1
            return val
        else:
            raise StopIteration


class ClassRoom:
    def __init__(self):
        self._students = []

    def add(self, student: Student):
        self._students.append(student)

    def __iter__(self):
        return ClassRoomIterator(self._students)


if __name__ == "__main__":
    class_room = ClassRoom()
    for num in range(1, 31):
        class_room.add(Student(f"N{num}", f"L{num}", f"N{num}L{num}"))
    iterator = iter(class_room)
    for element in iterator:
        print(element)
