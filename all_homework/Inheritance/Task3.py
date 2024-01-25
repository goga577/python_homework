"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""
class SpaceObject:
    def __init__(self, size):
        self.size = size
class Star(SpaceObject):
    def __init__(self,size, luminance):
        super().__init__(size)
        self.luminance = luminance
    def give_me_light(self):
        print (f'Звезда, размером {self.size} светит очень ярко - {self.luminance} единиц по шкале Елены Летучей')
class Planet(SpaceObject):
    def __init__(self, size, population, speed_population):
        super().__init__(size) #Стойте
        self.population = population
        self.speed_population = speed_population
    def what_population_in_future(self, year_for_speed):
        print (f'Популяция за {year_for_speed} вырастет с {self.population} до {self.population + (self.speed_population * year_for_speed)}')
Mars = Planet(12,45,6)
Mars.what_population_in_future(5)
Sun = Star(56, 87)
Sun.give_me_light()