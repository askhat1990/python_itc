name = input("Enter your name: ")
last_name = input("Enter your last name: ")
born = int(input("Какого ты года?: "))
name = name.capitalize()
last_name = last_name.capitalize()
if born < 1910:
    print("Ты что бессмертный? Год не должен быть меньше 1910")
if born > 1910:
    city = input("WHere are you from?")
    print(f'''
    Имя: {name} 
    ФАмилия: {last_name} 
    Год Рождения: {born} 
    Город: {city} 
    ''')