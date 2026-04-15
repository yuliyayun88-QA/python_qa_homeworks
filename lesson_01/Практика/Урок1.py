weekDays = ["понедельник", "вторник", "среда", "четверг", "пятница",
            "суббота", "воскресенье"]

length = len(weekDays)
print(len(weekDays))

день1 = weekDays[0]
print(день1)
день7 = weekDays[7]
print(weekDays[6])


def sum_numbers(num_1, num_2):
    print("слагаемое 1 =", num_1)
    print("слагаемое 2 =", num_2)
    result = num_1+num_2
    print("сумма = ", result)
    return result


def multiply(x, y):
    return x*y


def minus(a, b):
    return a-b


def delen(p, t):
    return p/t


def kalkul(a, b, c, d, e):
    return a+b*c-d/e


x = sum_numbers(10000, 42)
print(x)

m = multiply(3, 4)
print(m)

q = minus(5, 3)
print(q)

w = delen(15, 3)
print(w)

answer = kalkul(2, 3, 4, 5, 3)
print("ответ= ", answer)


def greet(num, numm):
    print("привет ", +num, numm)


greet(123, "Ann")


def funcA():
    print("Начали А")
    funcB()
    print("Закончили А")


def funcB():
    print("Начали В")
    funcC()
    print("Закончили В")


def funcC():
    print("Начали С")
    print("Закончили С")


funcA()
