def is_year_leap(year):
    result = True if year % 4 == 0 else False
    print('Год ', year, ':', result)
    return result


year = int(input('Введите год - '))

is_year_leap(year)
