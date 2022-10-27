# import random
from pprint import pprint

# a = set()
# a.update([324,543,23,3,1,5,6,7,8])
# print(a)
# b = {32,34,645654,36546,54,6,3534,52}

# print(a.intersection(b))

# menu = {}
# menu['besh_barmak']=130
# print(menu)
# menu['besh_barmak']=135
# print( = menu)

# a = random.randint(1, 9)
# b = random.randint(1, 9)

# print(f'How much is {a} * {b}?' )
# c = int(input())

# if a*b==c:
#     print('Correct')

# else:
#     print(f'Неправильный ответ. Верный ответ: {a*b}')



# print(False or (True or (2 < 3)))
# print((2 > 3) and (3 < 4) or True)
# print((not True or 5**2 != 1000) and not False)
# print(not ((None == False) and (25 >= 25)) and ("123" == 123))

# # Пример выполнения задания:
# print(False or (True or (2 < 3)))
# print(False or (True or True))
# print(False or True)
# print(True)
# print(False or True and 2<3 or False)

# name = input("Enter your name: ")
# last_name = input("Enter your last name: ")
# born = int(input("Какого ты года?: "))
# from1 = input("WHere are you from?")
# anketa = {}
# if born < 1910:
#     print("Ты что бессмертный? Дата рождения не может быть меньше 1910")


anketa['name']={name}
anketa['last name']={last_name}
anketa['born']={born}
anketa['from']={from1}
pprint(anketa)
anketa['name'] = [input("Enter your name: ")]
anketa['last name'] = [input("Enter your last name: ")]
anketa['born'] = [int(input("Enter your date of birth: "))]
print (anketa['born'])
if int(anketa['born']) < 1910:
    print("Ты что бессмертный? Дата рождения не может быть меньше 1910")

else:
    anketa['born'] = [input("Enter your date of birth: ").capitalize()]
    anketa['from'] = [input("WHere are you from: ").capitalize()]
    pprint(anketa)

# wather_dict = {'base': 'stations',
#  'clouds': {'all': 100},
#  'datetime': '2022-10-26 11:33:21.774524',
#  'main': {'feels_like': 6.57,
#           'grnd_level': 925,
#           'humidity': 71,
#           'pressure': 1022,
#           'sea_level': 1022,
#           'temp': 9.18,
#           'temp_max': 9.18,
#           'temp_min': 9.18},
#  'name': 'Almaty',
#  'rain': {'1h': 1.26},
#  'sys': {'country': 'KZ', 'sunrise': 1666747131, 'sunset': 1666785198},
#  'timezone': 21600,
#  'visibility': 10000,
#  'weather': [{'description': 'moderate rain',
#               'icon': '10d',
#               'id': 501,
#               'main': 'Rain'}],
#  'wind': {'deg': 262, 'gust': 9.09, 'speed': 4.99}}

# # pprint(wather_dict)
 
# print(f'''
#  Дата: {wather_dict['datetime'][0:10]}
# Время: {wather_dict['datetime'][11:16]}
# Погода в городе: {wather_dict['name']}
# Температура:  {wather_dict['main']['temp']}°C  
# Описание: moderate rain
# Облачность: 100
# Влажность: 71
# Давление: 1022  мм.рт.ст
# Скорость ветра: 4.99
# ''')