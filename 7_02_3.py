# class Vector:
#     def __init__(self, *args):
#         self.cords = args
#     def get_coords(self):
#         return self.cords[0]
#     def __add__(self, other):
#         if len(self.cords) != len(other.cords):
#             raise TypeError('Размерности векторов не совпадают')
#         else:
#             check = True
#             newcords = []
#             for i in range(len(self.cords)):
#                 newcords.append(self.cords[i] + other.cords[i])
#                 if type(self.cords[i] + other.cords[i]) != int:
#                     check = False
#             newcords = tuple(newcords)
#             if check:
#                 return VectorInt(newcords)
#             else:
#                 return Vector(newcords)
#     def __sub__(self, other):
#         if len(self.cords) != len(other.cords):
#             raise TypeError('Размерности векторов не совпадают')
#         else:
#             check = True
#             newcords = []
#             for i in range(len(self.cords)):
#                 newcords.append(self.cords[i] - other.cords[i])
#                 if type(self.cords[i] - other.cords[i]) != int:
#                     check = False
#             newcords = tuple(newcords)
#             if check:
#                 return VectorInt(newcords)
#             else:
#                 return Vector(newcords)
# class VectorInt(Vector):
#     def __init__(self, *args):
#         super().__init__(*args)
#         for coordinate in self.cords:
#             if type(coordinate) != int:
#                 raise ValueError('Координаты должны быть целыми числами')
# if __name__ == '__main__':
#     v1 = Vector(1, 2, 3)
#     v2 = Vector(3, 4, 5)
#     assert (v1 + v2).get_coords() == (4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
#     assert (v1 - v2).get_coords() == (-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"
#     v = VectorInt(1, 2, 3, 4)
#     assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"
#     try:
#         v = VectorInt(1, 2, 3.4, 4)
#     except ValueError:
#         assert True
#     else:
#         assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"
#
#     v1 = VectorInt(1, 2, 3, 4)
#     v2 = VectorInt(4, 2, 3, 4)
#     v3 = Vector(1, 2, 3, 4)
#     v = v1 + v2
#     assert type(
#         v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
#     v = v1 + v3
#     assert type(
#         v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
#     print("passed")

class Student:
    def __init__(self, fio, group):
        self._fio = fio
        self._group = group
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"

class Mentor:
    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject

class Lector(Mentor):
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        student.add_lect_marks(mark)

    def __str__(self):
        return f"Лектор: {self._fio}: предмет: {self._subject}"

class Reviewer(Mentor):
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        student.add_house_marks(mark)

    def __str__(self):
        return f"Эксперт: {self._fio}: предмет {self._subject}"