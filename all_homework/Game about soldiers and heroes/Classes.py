"""
class gameobject:
- id
- team
class Hero(gameobject):
- уровень
- метод лвл уп
class Soldier(gameobject):
- метод следовать
team1 = []
team2 = []
создать 2 героя
в цикле создать по 40 солдат, рандомно раскидать по разным спискам
измерить длинну обоих списков, повысить уровень героя у которого больше солдат
отправить солдат следовать за этим героем
"""
class game_object:
    def __init__(self, id, team):
        self.id = id
        self.team = team
class Hero(game_object):
    def __init__(self, id, team, lvl=1):
        super().__init__(id, team)
        self.lvl = lvl
    def give_me_lvl(self):
        self.lvl += 1
        print(f"УРА! Герой под номером {self.id} повысил свой уровень! Теперь он  {self.lvl} lvl'a!")
class Soldier(game_object):
    def follow_to_hero(self, hero):
        print(f'Я солдат под номером {self.id} и я встаю под знамёна бравого героя {hero.id}')