password = 'test12345'

if (password == "test12345"):
    print("Passed")
else:
    print("Неверно")


# Как-то получить от пользователя оценку
rate_as_str = input("Оцените работу оператора от 1 до 5: ")  # str

rate = int(rate_as_str)  # int

# Проверить, что оценка от 1 до 5
if (rate < 1):
    rate = 1

if (rate > 5):
    rate = 5

print(rate)

# В зависимости о оценки предложить обратную связь
feedback = ''

if rate == 1:
    feedback = input("Расскажите, что нам улучшить: ")
elif rate == 2:
    feedback = input('Расскажите, что смутило: ')
elif rate == 3:
    feedback = input('Расскажите, как сать лучше: ')
elif rate == 4:
    feedback = input('Расскажите, почемуне 5? ')
else:
    feedback = input('Расскажите,за что похвалить оператора: ')

print(feedback)
