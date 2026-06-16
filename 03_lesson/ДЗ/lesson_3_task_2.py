from smartphone import Smartphone


catalog = [
   Smartphone('Samsung', 'Note', +79263652525),
   Smartphone('iPhone ', 'proMax', +79254561236),
   Smartphone('Nokia', 'Lumia', +79163852423),
   Smartphone('Huawei', 'Nova', +79163952413),
   Smartphone('Tecno', 'Spark', +79173862721)
   ]

for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. {smartphone.number}')
