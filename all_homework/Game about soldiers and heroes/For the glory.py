import random
import Classes
def give_me_id(): #Генерация id
    return random.randint(1,4221)
def give_me_team(): #Выбор команды
    return random.randint(1,2)
def give_me_soldier(): #Генерация солдата
    soldier_id = give_me_id()
    soldier_team = give_me_team()
    new_soldier = Classes.Soldier(id = soldier_id, team =soldier_team)
    return new_soldier
def for_the_glory(team_of_hero_winner,hero): #Функция, чтобы каждый солдат следовал за гером
    for object in team_of_hero_winner: #Или, возможно, это как то лучше можно реализовать
        if not isinstance(object, Classes.Hero): #Проверка, что объект не образован от класса 'Hero'
            object.follow_to_hero(hero)


id_for_hero_one = give_me_id()
team = give_me_team() #Генерация атрибутов для 1 героя

hero_1 = Classes.Hero(id_for_hero_one, team) #Создание 1 героя

id_for_hero_two = give_me_id()
team_for_two_hero = give_me_team() #Генерация значений для 2 героя

while hero_1.id == id_for_hero_two or hero_1.team == team_for_two_hero: #Во избежания повторов id у 2 героев
    id_for_hero_two = give_me_id()
    team_for_two_hero = give_me_team()
hero_2 = Classes.Hero(id = id_for_hero_two, team = team_for_two_hero)

list_of_id = [] #Список использованных id-шников
list_of_id.append(id_for_hero_one,)
list_of_id.append(id_for_hero_two)#Id уникальные чтобы были

team_hero_1=[]
team_hero_1.append(hero_1)
team_hero_2 =[]
team_hero_2.append(hero_2)

for i in range(40):
    soldier_for_distribution = give_me_soldier()
    while soldier_for_distribution.id in list_of_id: #Проверка, что id уникальный
        soldier_for_distribution = give_me_soldier()
    list_of_id.append(soldier_for_distribution.id) #Добавляем id в список использованных
    if soldier_for_distribution.team == 1: #распределение по командам
        team_hero_1.append(soldier_for_distribution)
    else:
        team_hero_2.append(soldier_for_distribution)
print('И вот...40 воинов выбрали свои судьбы...')

if len(team_hero_1) > len(team_hero_2):
    print(f'Армия героя {hero_1.id} из {len(team_hero_1)} бравых воинов выдвигается!')
    hero_1.give_me_lvl()
    for_the_glory(team_hero_1, team_hero_1[0])
elif len(team_hero_1) == len(team_hero_2):
    print('Неделимая армия 2-х героев выдвигается!') #Дружба победила
else:
    print(f'Армия героя {hero_2.id} из {len(team_hero_2)} бравых воинов выдвигается!')
    for_the_glory(team_hero_2, team_hero_2[0])
