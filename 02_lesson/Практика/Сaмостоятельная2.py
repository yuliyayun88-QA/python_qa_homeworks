# import math


# employee_list = ['John Snow', 'Piter Pen', 'Drakula', 'IvanIV', 'Moana',
#                  'Juilet']

# print(employee_list[1] + ', ' + employee_list[-2])

# second_element = employee_list[1]  # Второй вариант
# second_element_from_end = employee_list[-2]
# print(f"{second_element}, {second_element_from_end}")


# def dev_by_three(num):
#     func = num % 3
#     return func


# ans = dev_by_three(7)

# if ans == 0:
#     print('Делится на 3? ' + 'Yes')
# else:
#     print('Делится на 3? ' + 'No')


# def dev_by_three(number):  # Правильный ответ
#     return "Да" if number % 3 == 0 else "Нет"


# num = int(input("Введите число: "))
# result = dev_by_three(num)
# print(f"Делится ли на три {num}? - {result}")


# # import math  # из-за flake8 перенесла в начало файла


# def min_boxes(item_num):
#     return (item_num / 5) if item_num % 5 == 0 else math.ceil(item_num / 5)


# item_num = int(input('Введите числ: '))
# q = min_boxes(item_num)
# print('Минимальное количество коробок = ', q)


# # import math # уже содана ранее


# def min_boxes(items):
#     return math.ceil(items / 5)


# num_items = int(input("Введите количество предметов: "))
# print(f"Минимальное количество коробок: {min_boxes(num_items)}")


# n = int(input("Введите число:"))  # Верное решение


# def check_divisibility(n):
#     for i in range(1, n + 1):
#         if i % 4 == 0:
#             print(f"{i} - Делится и на 2, и на 4")
#         elif i % 2 == 0:
#             print(f"{i} - Делится на 2, но не на 4")
#         else:
#             print(i)


# check_divisibility(n)

# month = int(input('введите месяц '))


# def quarter_of_year(month):
#     if 1 <= month <= 3:
#         return 'Квартал 1'
#     elif 4 <= month <= 6:
#         return 'Квартал 2'
#     elif 7 <= month <= 9:
#         return 'Квартал 3'
#     else:
#         return 'Квартал 4'


# print(quarter_of_year(month))


# lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]

# for lst in lst:
#     if lst > 15 and lst % 3 == 0:
#         print(lst)


lst = list(range(25, 4, -5))
print(lst)

# var_1 = 50
# var_2 = 5

# q = var_1
# var_1 = var_2
# var_2 = q

# print(f'var_1 = {var_1}')
# print(f'var_2 = {var_2}')
