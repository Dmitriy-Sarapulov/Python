import sys
import os
import unittest
# Этими 3 командами мы обращаемся к системе через код, для того,что бы потом указать нужный путь
sys.path.append(os.path.join(os.getcwd(), '..')) # Указываем путь в корень каталога
# getcwd - получение текущего рабочего каталога.
#from HW8.task1 import Matrix # таким образом мы берем класс из другой папки в данном каталоге
# можем брать оттуда все что угодно
# os.path - связка для работы с операционной системой.

# Дескрипторы и метаклассы!!!!!


# class Worker:
#     # класс работник
#     def __init__(self, name, surname, hours, rate):
#         self.name = name
#         self.surname = surname
#         self.hours = hours
#         self.rate = rate

#     def total_pofit(self):
#         #Рассчет зарплаты
#         return self.hours * self.rate

# OBJ = Worker("Иван", "Иванов", 10, -100)
# print(OBJ.total_profit())

# OBJ.hours = 20
# OBJ.rate = -200
# print(OBJ.total_pofit())

# Решение проблемы традиционным способом, через геттеры и сеттеры

class Worker:
    # делаем атрибуты защищенными
    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname

        if hours < 0:
            raise ValueError("Значение часов не может быть отрицательным") # поднимаем исключение
        self._hours = hours

        if rate < 0:
            raise ValueError("Значение ставки не может быть отрицательным") # поднимаем исключение
        self._hours = hours

# Для создания свойства-геттера над свойством ставится аннотация @property
# Геттер нужен для того,что бы вернуть значение защищенного или приватного атрибута
@property
def hours(self):
    # геттер
    return self._hours

# сеттерs


# Сеттер (установщик) в Python – это метод, который используется для установки значения свойства. 
# В объектно-ориентированном программировании очень полезно устанавливать значение частных атрибутов в классе. 
# Как правило, геттеры и сеттеры в основном используются для обеспечения инкапсуляции данных в ООП.


# Для совздания свойства сеттера над свойством устанавливается аннотация
# Имя_свойства_геттера.setter
@hours.setter
def hours(self, value):
    # сеттер
    if value < 0:
        raise ValueError("Значение часов не может быть отрицательным")
    self._hours = value

def total_profit(self):
    # Вычисляем зарплату
    return self.hours * self.rate

OBJ = Worker('Иван', 'Иванов', 10, 100)
print(OBJ.total_profit())

OBJ.hours = -10
OBJ.rate = 100

# Дескрипторы - это мощный протокол общего назначения. Это механизм, 
# лежащий в основе свойств, методов, статических методов, методов класса и super (). 
# Они используются в самом Python для реализации новых классов стилей, представленных в версии 2.2. 
# Дескрипторы упрощают базовый C-код и предлагают гибкий набор новых инструментов для повседневных программPython.

# Новый протакол дескрипторов

class Non_negative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        # owner - владелец атрибута - <class '__main__.Worker'>
        # my_attr - имя фтрибута владельца -hours, rate
        self.my_attr = my_attr


class Worker:
    # имя атрибута, который делаем, дескриптором, в конструктор не передаем
    hours = Non_negative() #мы наши атрибуты делаем экземплярами класса Non_negative
    rate = Non_negative()


    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.rate = rate

    def total_pofit(self):
        #Рассчет зарплаты
        return self.hours * self.rate

OBJ = Worker("Иван", "Иванов", 10, -100)
print(OBJ.total_profit())

OBJ.hours = 20
OBJ.rate = -200
print(OBJ.total_pofit())
# Остановился на 37:51 минуте