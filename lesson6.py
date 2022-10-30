# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение

# lst = [1, 1, 2, 3, 5, 1, 5, 3, 10] #-> [2, 10]

# def sort(lst):
#     uniq_elements = set()
#     for el in lst:
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
#     while '*' in lst:
#         index = lst.index('*')
#         result = lst[index - 1] * lst[index + 1]
#         lst = lst[:index - 1] + [result] + lst[index + 2:]
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


#print(parse("(1+2)*3"))