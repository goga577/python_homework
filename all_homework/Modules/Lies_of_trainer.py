import random
def give_me_phone():
    random_phone = str(random.randint(7, 8)) + "-" + str(random.randint(286, 955)) + "-" + \
                   str(random.randint(155, 438)) + "-" + str(random.randint(38, 87)) + " " + \
                   str(random.randint(10, 76))  # Генерируем телефон
    return random_phone

def give_me_name():
    name_list = ["Антон", "Степан", "Виктор", "Евгений", "Александр", "Николай", "Святослав", "Артур", "Никита", "Иван",
                 "Оккам", "Платон"]
    surname_list = ["Говрилов", "Макушев", "Блинов", "Шишкин", "Медведев", "Любенко", "Дроздов", "Галицкий", "Горюнов",
                    "Грин", "Певчих", "Лёдов"]
    random_name = random.choice(name_list) + " " + random.choice(surname_list) #Генерируем имя несуществующего человека
    return random_name

def give_me_trainer () -> dict:
    name_list = ["Антон", "Степан", "Виктор", "Евгений", "Александр", "Николай", "Святослав", "Артур", "Никита", "Иван", "Оккам", "Платон"]
    surname_list = ["Говрилов", "Макушев", "Блинов", "Шишкин", "Медведев", "Любенко", "Дроздов", "Галицкий", "Горюнов", "Грин", "Певчих", "Лёдов"]
    trainer_dict = dict ()
    for i in range (len(name_list)):
        random_name = random.choice (name_list) #Выбор рандомного имени
        name_list.remove(random_name) #Удаляем имя, чтобы оно не повторялось
        random_surname = random.choice (surname_list)
        surname_list.remove(random_surname) #Аналогично с фамилией
        full_random_name = random_name + " " + random_surname #Получаем фамилию и имя вымышленного человека в одной строке
        random_phone = give_me_phone()
        trainer_dict [random_phone] = full_random_name
    return trainer_dict