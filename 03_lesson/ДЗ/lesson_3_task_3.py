from address import Address
from mailing import Mailing

to_address = Address(420098, 'Казань', 'Сухая', 2, 53)
from_address = Address(302024, 'Орел', 'Степная', 45, 3)

send_mail = Mailing(to_address, from_address, 580.8, '3020245896352')

print(send_mail)
