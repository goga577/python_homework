"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""
import Hero
class Magican(Hero.Hero):
    def hello(self):
        print (f'{self.name} машет тебе ручкой')

Azmodan = Magican('Азмодан')
Azmodan.heal() #Метод родителя
Azmodan.hello() #Метод наследника