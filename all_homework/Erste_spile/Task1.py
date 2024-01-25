import random
class Unit:
    def __init__(self, name):
        self.HP = 38
        self.name = name
        self.armor = 12
        self.status = 'It is life!'
    def dead (self):
        self.status = 'It is dead'
        print (f'{self.name}')
    def attack_enemy(self, enemy_obj):
        hit = random.randint(4,9)
        enemy_obj.armor -= hit
        if enemy_obj.armor <= 0:
            enemy_obj.HP += enemy_obj.armor
            if enemy_obj.HP <= 0:
                enemy_obj.dead()
                print (f'{enemy_obj.name} ПАЛ ОТ РУКИ {self.name}')
class Ork_podkaster(Unit):
    def __init__(self,name):
        Unit.__init__(self,name)
class Uncle_Burn(Unit):
    def __init__(self,name):
        Unit.__init__(self,name)

Orkpod =Ork_podkaster('Orkpod')
Burn = Uncle_Burn('Uncle_Burn')
while Burn.status != 'It is dead' and Orkpod.status != 'It is dead':
    Burn.attack_enemy(Orkpod)
    Orkpod.attack_enemy(Burn)
