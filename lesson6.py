# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение

# lst = [1, 1, 2, 3, 5, 1, 5, 3, 10] #-> [2, 10]

# def sort(lst):
#     uniq_elements = set()
#     for el in list:
#         if el not in uniq_elements:
#             uniq_elements.add(el)
#         else:
#             uniq_elements.discard(el)
#     s = list(uniq_elements)
#     s.sort()
#     return s

#'(1+2)*3'

# def parse(s):
#     result = []
#     for symb in s:
#         if symb.isdigit():
#             digit +=symb
#         elif symb in ['(', ')']:
#             if digit:
#                 result.append(float(digit))
#                 digit = ''
#             result.append(symb)
#         else:
#             if digit:
#                 result.append(float(digit))
#                 digit = ''
#             result.append(symb)
#     else:
#         if digit:
#             result.append(float(digit))
#     return result
# print(parse("(1+2)*3"))