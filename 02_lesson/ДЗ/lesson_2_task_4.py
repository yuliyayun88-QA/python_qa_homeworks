def fizz_buzz(n):
    lst = list(range(1, n+1))
    print('Список', lst)
    L = len(lst)
    print('количесво в списке', L)
    for i in range(1, L+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)


n = int(input('Введите количественную длину списка: '))


fizz_buzz(n)
