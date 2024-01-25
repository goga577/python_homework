"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""
class Duck:
    def __init__(self):
        pass
    def give_me_voice(self):
        print ('Уточка говорит кря-кря')
    def look_me(self):
        print('Уточка носит перья...')
class Human:
    def __init__(self):
        pass
    def look_me(self):
        print('Человек носит одежду')
    def give_me_voice(self):
        print('Человек имитирует кряканье')

ork_pod = Duck()
Uncle_Bjorn = Human()
list_of_object = [ork_pod, Uncle_Bjorn]

yes = 'угу'
for i in list_of_object:
    i.look_me()
    i.give_me_voice()