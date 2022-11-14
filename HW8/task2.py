# Задание 2.
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Единственный класс этого проекта — одежда (класс Clothes).
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
# для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать
# абстрактный класс для единственного класса проекта,
# проверить на практике работу декоратора @property
# Пример:
# Расход ткани на пальто = 1.27
# Расход ткани на костюм = 20.30
# Общий расход ткани = 21.57
# Два класса: абстрактный и Clothes



class Clothes:

    def __init__(self, v, h):
        self.v = v
        self.h = h

    def consumption_v(self):
        print(f"Количество ткани для пальто = {self.v / 6.5 + 0.5}")
        return self.v / 6.5 + 0.5

    def consumption_h(self):
        print(f"Количество ткани для костюма = {2 * self.h + 0.3}")
        return 2 * self.h + 0.3

    def common_cons(self):
        return (self.v / 6.5 + 0.5) + (2 * self.h + 0.3)

    def __add__(self, other):
        return Clothes(self.v + other.v, self.h + other.h)

    def __str__(self):
        return f"{self.v, self.h}"


a = Clothes(5, 7)
b = Clothes(5, 7)
a.consumption_h()
a.consumption_v()
print(f"Итого расход ткани = {a.common_cons()}")
print(a)
print(b)
c = a + b
print(c)