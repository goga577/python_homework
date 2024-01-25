"""
В классе Hero из предыдущего занятия добавьте приватное свойство lvl.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""
import random
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.lvl = 'Даже не гражданин'
        self.attack = 17
        self. armor = 15
    def hero_hit(self, name_enemy):
        print (f'{self.name} бьёт по {name_enemy}')
    def heal(self):
        heal = random.randint(1, 8)
        print (f'{self.name} вылечил себя на {heal}')
        self.hp += heal
    def get_me_lvl(self):
        return self.lvl
    def change_lvl_if_victory(self):
        self.lvl = 'Победитель арены'
    def you_are_dead(self):
        self.lvl = 'ДАЖЕ НЕ ДАЖЕ'