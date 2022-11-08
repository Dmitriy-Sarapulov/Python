# Урок 10. Возможна ли жизнь без PIP? Продолжение
# Юнит тесты

# Тесты - это код, проверяющий работу кода.

# Компонентное, модульное или юнит тестирование.

# Хороший тест:
# Корректный - тестирует то,что нужно проверить
# Понятен читателю
# Крнкретный - проверяет то что надо.

# Оператор assert - через этот оператор делается имитация юнит теста.

def write_data(file, data):
    assert file, 'write_data: файл не определен!' # не сработает, когда нет файла.

def assert_equal(x,y):
    assert x == y, "{} != {}".format(x, y) # x == y(true/falce?) 
    # "{} != {}".format(x, y) сообщение которе передается только при Falce

# Как использовать assert(assert - используется только на этапе отладки)

"""Фамилия Имя Часов Ставка
    Иванов Иван 45 400 """

from collections import namedtuple


Salary = namedtuple('Salary', ('surname', 'name', 'worked', 'rate')) # Создаем именованный кортеж

# Иванов Иван 45 400

def get_salary(line):
    # вычисление зарплаты
    line = line.split()

    if line:
        data = Salary(*line)
        # data->Salaty(surname = 'Иванов' name = 'Иван' worked = '45' rate = '400')
        fio = ' '.join((data.name, data.surname))
        salary = int(data.worked) * int(data.rate)
        res = (fio, salary)
        # res -> ('Иванов Иван', 18 000)
    else:
        res = ()
    return res


arr = []
def decor(func): #Декоратор который помещает результаты в список(итерируемый объект)
    def wrap(*args, **kwargs):
        arr.append(func)
    return wrap

def res_1(): # Находится в этом списке и вызывает все функции сразу
    for el in arr:
        el()



@decor
def test_get_salary_sum():
# первый тест
    assert get_salary('Иванов Иван 45 400')[1] == 18000, 'Неверная сумма'

@decor
def test_get_salary_fio():
# второй тест
    assert get_salary('Иванов Иван 45 400')[0] == 'Иван Иванов', 'Неверное Имя'

@decor
def test_get_salary_empty():
# третий тест
    assert get_salary('') == (), 'Не пустые значения'

if __name__ == '__main__':
    res_1()


# В реально жизни, для написания тестов применяются 2 библиотеки pytest and unittest

import unittest

class Test_Split_Function(unittest.Test_Case):
    def set_up(self):
        # ВЫполнить настройку тестов, если не обходимо.
        pass
    def tear_down(self):
        # Выполнить завершающие действия, если необходимо
        pass
    # def test_simple_string(self):
    #     r = split('GOOG 100 490.50')
    #     self.assert_equal(r, ['GOOG', '100', '490.50'])
    # def test_type_convert(self):
    #     r = split('GOOG 100 490.50', [str, int, float])
    #     self.assert_equal(r, ['GOOG', 100, 490.50])


#3 способа запуска тестов

# 1) Через конфигурации, запускаем файл с тестами, как будто это обычный пайтон скрипт.
# если не обходимо обозначить тест, нужно написать префикс test_(в начале!)
# 2) Опция в pycharm unittest
# 3) Запуск в ручную,через код