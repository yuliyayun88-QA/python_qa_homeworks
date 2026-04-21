import math


def square(side):
    square_area = (side * side)
    return math.ceil(square_area)


side = float(input('Введите длину стороны квадрата: '))

answer = square(side)
print('Ответ:', answer)
