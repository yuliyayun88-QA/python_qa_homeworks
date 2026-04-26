""" user_login = 'adam'
user_password = 'qwerty123456'

login = input('Login: ')
password = input('Password: ')

if (login == user_login) and (password == user_password):
    print('Secret is open')
else:
    print('Locked') """


crit = 'red'
crit1 = 'lock'

color = input('color: ')
feature = input('feature: ')

if (color == crit) or (feature == crit1):
    print('Buy it!')
else:
    print('Похожу,еще посмотрю')
