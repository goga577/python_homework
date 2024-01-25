import random
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.lvl = 1
        self.attack = 17
        self. armor = 15
    def hero_hit(self, name_enemy):
        print (f'{self.name} бьёт по {name_enemy}')
    def heal(self):
        heal = random.randint(1, 8)
        print (f'{self.name} вылечил себя на {heal}')
        self.hp += heal