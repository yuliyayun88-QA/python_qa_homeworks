def month_to_season(number):
    if 3 <= number <= 5:
        print('Весна')
    elif 6 <= number <= 8:
        print('Лето')
    elif 9 <= number <= 11:
        print('Осень')
    elif number := (1, 2, 12):
        print('Зима')
    else:
        print('Неверное значение месяца года')


number = int(input('Введите числовое значение месяца (от 1 до 12): '))

month_to_season(number)
