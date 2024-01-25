"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English,Japenese]
1 - [English]
"""
amount_students = int (input ("Введите количество учеников: "))
languages = []
while amount_students > 0:
    amount_smart = int(input("Введите количество учеников "))
    amount_students -= amount_smart
    language = input ("Введите языки или введите off для завершения")
    var = []
    while language != "off":
        var.append(language)
    languages.append(var)
set1 = set(languages[0])
set2 = set(languages[1])
set3 = set(languages[2])
print (se1|set2|set3)
print (set1 &set2&set3) #Решение с занятия