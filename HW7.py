# Задание 1.
# Создать класс TrafficLight (светофор)
# и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
# В рамках метода running реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.
# Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
# Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# 
# from time import sleep


# class TrafficLight:
#     color = ['Красный', 'Желтый', 'Зеленый']

#     def running(self):
#         lst = [7, 2, 5]
#         for sec in range(3):
#             print(self.color[sec])
#             sleep(lst[sec])


# t = TrafficLight()
# t.running()

# Задание 2.
# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.
# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т

# class Road:
#     mass = 25
#     thickness = 0.01

#     def __init__(self, withd, length):
#         self._withd = withd
#         self._length = length

#     def formula(self, mult_thickness):
#         result = self.mass * self._length * self._withd * self.thickness * mult_thickness
#         return str(f"{result}кг = {result / 1000} т")


# r = Road(20, 5000)
# print(r.formula(5))

# Задание 3.
# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
# __str__(self) - вызывается функциями str,print и format. Возвращает строковое представление объекта.

# dic_1 = {"wage": 15000, "bonus": 1500}

# class Worker:
#     name = 'Anton'
#     surname = 'Semenov'
#     position = 'Master'
#     _income = dic_1


# w = Worker()
# print(w.__dict__)
# print(type(w))


# class Position(Worker):
#     def get_full_name(self):
#         print(f"Имя сотрудника: {self.name} Фамилия: {self.surname}")

#     def get_total_income(self):
#         print(f"Сотрудник заработал {dic_1['wage']}рублей + премия - {dic_1['bonus']} рублей,"
#               f"\nитого: {dic_1['wage'] + dic_1['bonus']}рублей")

# w1 = Position()
# print(w1.__dict__)
# print(type(w1))
# print("___________")

# anton = Position()
# anton.get_full_name()
# anton.get_total_income()

# Задание 4.
# Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
# speed, color, name, is_police (булево).
# А также публичные методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс публичный метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

# from random import randint


# class Car:
#     speed = randint(1, 100)

#     def __init__(self, speed, color="red", name="BMW", is_police=False):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police

#     def __str__(self):
#         return f"Объект с параметрами: {self.speed} {self.color} {self.name} {self.is_police}"

#     def go(self):
#         print(f"Машина поехала вперед со скоростью {self.speed}")

#     def stop(self):
#         print("Машина остановилась.")

#     def turn(self):
#         direction = randint(1, 2)
#         print("Машина повернула налево") if direction == 1 else print("Машина повернула направо")

#     def show_speed(self):
#         print(f"В данный момент машина движется со скоростью {self.speed}")


# class TownCar(Car):
#     def show_speed(self):
#         if self.speed > 60:
#             print("WARNING!!! Сбросьте скорость")
#             print(f"В данный момент машина движется со скоростью {self.speed}")

# class SportCar(Car):
#     "Спорт кар"

    
# class WorkCar(Car):
#     def show_speed(self):
#         print(f"В данный момент машина движется со скоростью {self.speed}")
#         if self.speed > 40:
#             print("WARNING!!! Сбросьте скорость")
#         else:
#             pass


# class PoliceCar(Car):
#     """child class from class Car"""


# town = TownCar(randint(1, 100), "Blue", "Mercedes")
# sport = SportCar(randint(1, 100), "Green", "Lada")
# work = WorkCar(randint(1, 100), "Black", "Audi")
# pol = PoliceCar(randint(1, 100), "Yellow", "Bugatti", True)

# print(f'TownCar = {town.__dict__}')
# town.show_speed()
# print(f'SportCar = {sport.__dict__}')
# print(f'WorkCar = {work.__dict__}')
# work.show_speed()
# print(f'PoliceCar = {pol.__dict__}')

# print(town)
# print(sport)
# print(work)
# print(pol)

# Задание 5.
# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

# class Stationery:
    
#     def __init__(self,title="Канцелярская принадлежность =)"):
#         self.title=title
#     def draw(self):
#         print("Запуск отрисовки.")

# class Pen(Stationery):
#     def draw(self):
#         print("Запуск отрисовки ручки? \nДа!")
# class Pencil(Stationery):
#     def draw(self):
#         print("Запуск отрисовки карандаша? \nДа!")
# class Handle(Stationery):
#     def draw(self):
#         print("Запуск отрисовки маркера? \nДа!")
#     def __str__(self):
#         return f'{self.title} хех'

# s = Stationery()
# pen = Pen("ручка")
# pencil = Pencil("карандаш")
# handle = Handle("маркер")

# print(type(pen))
# print(type(pencil))
# print(type(handle))
# print()
# s.draw()
# pen.draw()
# pencil.draw()
# handle.draw()