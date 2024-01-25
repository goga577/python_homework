import random
def give_me_lie_city ():
    list_city = ["Санкт-Петербург", "Москва", "Екатеринбург", "Томск", "Краснодар", "Красноярск", "Омск", "Новгород", "Владивосток", "Грозный"]
    return random.choice(list_city)
def give_me_lie_strasse ():
    list_strasse = ["Ленина", "Космонавтов", "Карла Маркса", "Пушкина", "Мира", "Фрунзе", "Юбилейная", "Великого Октября", "Герцена", "Первомайская", "Татищева", "Советская", "Ворошилова"]
    return "улица"+ " " + random.choice(list_strasse) + " " + str(random.randint (22, 96))
def lie_full_place ():
    list_city = ["Санкт-Петербург", "Москва", "Екатеринбург", "Томск", "Краснодар", "Красноярск", "Омск", "Новгород",
                 "Владивосток", "Грозный"]
    list_strasse = ["Ленина", "Космонавтов", "Карла Маркса", "Пушкина", "Мира", "Фрунзе", "Юбилейная", "Великого Октября", "Герцена", "Первомайская", "Татищева", "Советская", "Ворошилова"]
    dict_city = dict ()
    for city in list_city:
        lie_strasse = random.choice(list_strasse)
        dict_city [city] = "улица " + random.choice(list_strasse) + " " + str(random.randint (22, 96))
        list_strasse.remove(lie_strasse)
    return dict_city