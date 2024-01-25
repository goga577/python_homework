"""
В каждом заплыве участвуют два случайных спортсмена из разных сборных. Напиши программу для печати номеров спортсменов.

1) Программа должна запрашивать количество спортсменов в каждой сборной с сообщением: «Число участников сборной _:».
2) Затем должна печататься пара случайных спортсменов из разных сборных для заплыва в формате: «Пловец _ - пловец _».
"""
import random
from random import randint
def get_team ():
    num_team = int (input("Введите количество сборных: "))
    dict_team = dict()
    for i in range(0, num_team):
        num_player = int(input(f"Число участников сборной {i +1}: "))
        dict_team [i+1] = num_player
    return dict_team
def player_for_game ():
    dict_team = get_team()
    t1 = random.randint (1, len(dict_team.keys()))
    t2 = random.randint (1, len(dict_team.keys()))
    responce = True
    while t1 != t2 and responce != "off":
        print ("В заплыве участвуют:")
        print (f"Спорстмен под номером{random.randint (1, dict_team[t1])} из сборной {t1}")
        print (f"а также спортсмен под номером {random.randint(1, dict_team[t2])} из " +
               f"сборной {t2}")
        responce = input("Нужно ли сгенерировать ещё одну пару для заплыва? Off если нет").lower()
player_for_game()