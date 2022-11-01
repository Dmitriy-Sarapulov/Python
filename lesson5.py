# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# Объект типа Генератор: 

def check_even_1(numbers): # Обычный метод
    even = [] # который создает и заполняет массив(список)
    for num in numbers:
        if num % 2 == 0:
            even.append(num*num)
    return even # в Результате, заполенный список он хранит в памяти.

def check_even_3(numbers): # Это объект типа генератор не создает и не хранит массив
    for num in numbers:
        if num % 2 == 0:
            yield num * num # yield вернуть объект генератора. Мы не храним ничего в памяти,а делаем по запросу.

#Если не нужно обращаться к объекту по индексу, то можно использовать генератор.

# Если сравнивать по скорости и кол-ву задействованной памяти функцию list comprehension 
# и ф-цию filter, то фильтр будет эффективней.

def check_even_1(lst): # ф-ция с использованием LC 
    new_list = [i for i in lst if i % 2 == 0] # пример записи LC
    return new_list
# тут мы будем хранить список
def check_even_2(lst): # ф-ция с использованием filter и lambda
    new_list = filter(lambda x: x % 2 == 0, lst) # пример записи filter и lambda
    return new_list
# тут мы будем хранить объект ф-цуу фильтр.

# Исключения try except:

try:  # ТОчка где выполняется выражение
    res = 100/0
except ZeroDivisionError:  # отлов ошибки + генерация исключения(заявленного: ZeroDivisionError)
# можно сделать общее(Exception)
    print('На ноль делить нельзя')
else:  # Если except не сработал.
    print(f"Все хорошо, результат - {res}")
finally:  # Срабатывает всегда
    print("Программа завершена")

# класс-это исключение,исключение-это класс
# Создать класс исключение от класса Exception
# Сгенерировать исклчение в нужной точке программы
# Отловить и обработать

class OwnError(Exception): #создаем класс исключения(OwnError), он наследует от класса (Exception) 
# мы написали условия исключения
    def __init__(self, txt): #генерация исключения
        self.txt = txt

inp_data = input("Введите положительное число: ")

try:
    inp_data = int(inp_data)
    if inp_data < 0:
        raise OwnError("ВЫ ввели отрицательное число!") #rise генерация исключения(поднятие исключения)
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо, Ваше Число: {inp_data}")

# LC пименение.
# вывести только те элементы массива, который больше предыдущих.
lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lst = 