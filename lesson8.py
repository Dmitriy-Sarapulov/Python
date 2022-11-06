# Урок 8. Python: от простого к практике. Продолжение
# Перегрузка операторов
# Всегда ли нужно делать перегрузку инита? Ответ нет!

# __ibit__

class Myclass:
    def __init__(self, param): # Перегрузка
        self.param = param #Атрибут объекта, вмешаюсь в init, для передачи параметра.


obj = Myclass(1)

# Помимо того,что у нас есть инициализация объекта(__init__), у нас есть ещё и удаление(__del__).
# 

class Myclass:
    def __init__(self, param): # Перегрузка
        self.param = param #Атрибут объекта, вмешаюсь в init, для передачи параметра.

    def __del__(self): # Перегрузка
        print(f"Удаляем объект {self.param} класса Myclass")

mc = Myclass("text")
del mc # Удаляем объект класса Myclass, будет выполняться и без def __del__(Функции дел)

# __str__() - магический метод для отображения информации 
# об объекте класса для пользователей (например, для функций print, str)
# в клиентском коде нет необходимости явно вызывать встроеные функции, они итак выполняются

class Myclass:
    def __init__(self, param_1, param_2): # Перегрузка
        self.param_1 = param_1 #Атрибут объекта, вмешаюсь в init, для передачи параметра.
        self.param_2 = param_2
    def __str__(self): # Перегрузка
        return f"Объект с параметрами ({self.param_1}, {self.param_2} )"

mc = Myclass("text_1", "text_2")
print(mc)

# __add__() - Позволяет определить поведение объекта при прибавлении к нему другого. 
# self : Ссылка на экземпляр. other : Объект, который следует прибавить к текущему.


class Myclass:
    def __init__(self, whidth, height): # Перегрузка
        self.whidth = whidth #Атрибут объекта, вмешаюсь в init, для передачи параметра.
        self.height = height

    def __add__(self, other): # перегружаем, для того что бы вернуть новый экземпляр понятного класса(для Python)
        return Myclass(self.whidth + other.whidth, self.height + other.height)

    def __str__(self): # Перегрузка
        return f"Объект с параметрами ({self.whidth}, {self.height} )"

mc_1 = Myclass(10, 20)
mc_2 = Myclass(10, 20)
print(mc_1 + mc_2) # Объект с параметрами (40, 60)

# __setattr__() - Позволяет определить поведение экземпляра пользовательского типа 
# при попытке присвоения значения атрибуту.

class Myclass:
    def __setattr__(self, attr, value):
        print(self.__dict__)
        if attr == 'width': # Валидация
            self.__dict__[attr] = value
        else:
            print(f"Атрибут {attr} недопусьим")
        print(self.__dict__)

mc = Myclass
mc.width = 40 # Атрибут heght недопустим. Операции перегузки называют операции перхват.

#__getitem__ - Позволяет задать поведение при обращении к элементу контейнера.

class Class1:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return str(self.param)

class Class2:
    def __init__(self, *args): 
        self.my_list = []
        for el in args:
            self.my_list.append(Class1(el)) # Кладём сюда объекты класса 1
        print(self.my_list)

    def __getitem__(self, index): # Объукт отвечающий за взятие по интексу
        return self.my_list[index]

my_obj = Class2(10, True, "text")
print(my_obj.my_list[0]) # Беру первый элемент массива
# без __getitem__ Нельзя выполнить строчку ниже, так как у объекта нет индексов.
print(my_obj[1]) # за счёт перегрузки, делаем строчку выше.
print(my_obj[2])

# __call__ - Позволяет экземплярам пользовательских типов представляться объектами, поддерживающими вызов. 
# self : Ссылка на экземпляр. args : Любые позиционные и/или именованные аргументы.

class MyClass:
    def __init__(self, param):
        self.param = param

    def __call__(self, *args, **kwargs): # Позволяет вызвать объект класса как обычную ф-цию
        print("!")

obj = MyClass('!')
obj()

# __eq__ - Позволяет реализовать проверку на равенство для экземпляров пользовательских типов. self : 
# Ссылка на экземпляр. other : Объект с которым следует произвести сравнение (справа от оператора сравнения).

class MyClass:
    def __init__(self):
        self.x = 40

    def __eq__(self, y):
        print("!")

mc = MyClass()
print('Равно' if mc == 40 else "Не равно")
print('Равно' if mc == 41 else "Не равно")

# __iadd__ - 

class MyClass:
    def __init__(self, val):
        self.val = val

def __iadd__(self, other): # к атрибуту объекта прибавляет нужное значение.
    self.val += other
    return self

mc = MyClass(100)
print(mc.val)
mc += 200

# Интерфейсы. Абстрактные классы.

from abc import ABC, abstractclassmethod # без мпорта не сработает. Встроеный декоратор.

class MyAbstractClass(ABC):

    @abstractclassmethod # Напоминание о переопределении.Контролирует переопределен ли данный метод.
    def my_method_1(self):
        pass

    @abstractclassmethod # если есть декоратор абстрактного класса то переопределение обязательно
    def my_method_2(self):
        pass

class MyClass(MyAbstractClass):

    def my_method_1(self):
        pass

    def my_method_2(self):
        pass

mc = MyClass()
print(type(mc.my_method_2))

# @property - Функция property() используется для определения свойств в классах. Метод property() 
# обеспечивает интерфейс для атрибутов экземпляра класса. 
# Он инкапсулирует атрибуты экземпляров и предоставляет свойства, аналогично тому, как это работает в Java и C#.

class MyClass:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    @property # Мы будем работать с этим методом, как с атрибутом. Стилевая опция.
    def my_method(self):
        return f"Параметры, переданные в класс: " \
            f"{self.param_1}, {self.param_2}"

mc = MyClass()
print(mc.my_method())

# Статические методы и методы класса

class Auto:
    @staticmethod # Что бы не передавать self, только за счёт обертывания.(убрать лишнее, логически)
    def get_class_info(self): #self передаем всегда!!! пердавать нужно, но он не используется
        print("Детальная информация о классе")

a = Auto()
a.get_class_info()

# if __name__ == '__main__': - запсук модуля,как самостоятельной программы.

if __name__ == '__main__': # если мы запускаем модуль как самостоятельную программу, то:
    a = Auto() # Надо вот это выполнять.
    a.get_class_info()

# @classmethod

class User:
    pass

class NewClass:
    pass

class MyClass:
    @classmethod # Если им обернуть метод класса, то можно вызвать его через объект или сам класс.
    def my_method(cls): # метод класса (cls) - указание на класс
        print(cls.__dict__)

MyClass.my_method() # вызов метода через название класса
mc = MyClass()
print(mc.my_method())

# Атрибуты и встроенные методы объектов классов

class User:
    def __init__(self, name, login, passwd, email):
        self.name = name
        self.login = login
        self.passwd = passwd
        self.email = email
    
    def on_get_data(self):
        print(f"имя: {self.name}, логин: {self.login}, "
        f"пароль: {self.passwd}, email: {self.email}")
    
u = User('Ivan Ivanov', "IvIv", "11111", "iviv@mail.ru")
u.on_get_data()
print(f" name - {User.name}, \n module - {User.__module__}, \n"
f"__dict__ - {User.__dict__}, \n __bases__ - {User.__bases__}, \n"
f"__doc__ - {User.__doc__}, \n hash - {User.__hash__}") # это все характеристики объекта.

# Пример приложения с ООП

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Name and Surname: {self.name}, {self.surname}"

class Teacher(Person):
    def to_teach(self, subj, *pupils):
        for pupil in pupils:
            pupil.to_take(subj)

class Pupil(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.knowledges = []

    def to_take(self, subj):
        self.knowledges.append(subj)

class Subject:
    def __init__(self, *subjects):
        self.subjects = list(subjects)

s = Subject("maths", "phisics", "chemistry")
t = Teacher("Ivan", "Ivanov")
print(t)

p_1 = Pupil("Petr", "Petrov")
p_2 = Pupil("Sergey", "Sergeev")
p_3 = Pupil("Vladimir", "Vladimirov")
print(f'{p_1}, {p_2}, {p_3}')

t.to_teach(s, p_1, p_2, p_3)
print(p_1.knowledges[0].my_list())

