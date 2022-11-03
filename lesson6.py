# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение

lst = [1, 2, 3, 5, 1, 5, 3, 10] #-> [2, 10]

def sort(lst):
    uniq_elements = set() #создает множество set() из уникальных элементов
    for el in lst:
        if el not in uniq_elements:
            uniq_elements.add(el) # Если уникального элемента нет во множестве, то добавляем его
        else:
            uniq_elements.discard(el) # Если элемент уже есть там, то удаляем его(remove ломает программу)
    s = list(uniq_elements) #Создаем лист из уникальных элементов
    s.sort() # Сортируем существующий массив(список)
  
# анти паттерн:
# Ф-ия не может возвращать разные типы данных
# ф-ция map и filter тоже являются анти паттерном, но не жестким. 

'2+2'

def parse(s): # начинаем с парсинга parse - разобрать
    result = []
    digit = ''
    for symb in s:
        if symb.isdigit(): # узнаем,что это число
            digit +=symb
        elif symb in ['(', ')']: #исключаем скобки 
            if digit:
                result.append(float(digit))
                digit = ''
            result.append(symb)
        else:
            if digit:
                result.append(float(digit))
                digit = ''
            result.append(symb)
    else:
        if digit:
            result.append(float(digit))
    return result
print(parse("(1+2)*3"))

# "(1+2)*3"
# def parse(s):
#     result = []
#     digit = ''
#     for symb in s:
#         if symb.isdigit():
#             digit += symb
#         elif symb in ['(', ')']:
#             if digit:
#                 result.append(float(digit))
#                 digit = ''
#             result.append(symb)
#         else:
#             if digit:
#                 result.append(float(digit))
#             digit = ''
#             result.append(symb)
#     else:
#         if digit:
#             result.append(float(digit))
#     return result


# def calc(lst):
#     result = 0.0
#     while '*' in lst: # цикл поиска *
#         index = lst.index('*') #Вычисляем индекс элемента *
#         result = lst[index - 1] * lst[index + 1] # Ищем операнды(числа которые нужно умножить)
#         lst = lst[:index - 1] + [result] + lst[index + 2:] # мы не можем сложить массив и число, по этому ресулт делаем массивом
#     while '/' in lst:
#         index = lst.index('/')
#         result = lst[index - 1] / lst[index + 1]
#         lst = lst[:index - 1] + [result] + lst[index + 2:]
#     while '+' in lst:
#         index = lst.index('+')
#         result = lst[index - 1] + lst[index + 1]
#         lst = lst[:index - 1] + [result] + lst[index + 2:]
#     while '-' in lst:
#         index = lst.index('-')
#         result = lst[index - 1] - lst[index + 1]
#         lst = lst[:index - 1] + [result] + lst[index + 2:]
#     return result


# def brackets(lst):
#     while '(' in lst:
#         opening = lst.index('(')
#         closing = lst.index(')')
#         lst = lst[:opening] + [calc(lst[opening + 1:closing])] + lst[closing + 1:]
#     return lst


# s = "(1+2)*3"
# result = parse(s)
# result = brackets(result)
# print(calc(result))


# print(parse("(1+2)*3"))