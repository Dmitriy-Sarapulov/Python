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

