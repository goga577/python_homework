import Lies_of_trainer
import Lies_of_time
import random
def is_normal (mass, height):
    imt = mass/(height ** 2)
    if imt >= 18.5 and imt <= 25:
        return True
    else:
        return False

def give_me_consultation ():
    name_spec = Lies_of_trainer.give_me_name()
    time_start = input("Введите время, c которого вы бы хотели получить консультацию: ")
    if len(time_start.split(":")) == 2: #Если время введено с : ,то убираем его через len  и split
        time_start = int(time_start[0]) #так как split возвращает список, то берём из этого списка первый элемент
    time_for_consult = Lies_of_time.random_time(int(time_start),19, minutes = str(random.randint (12, 53)))
    mass = float (input("Введите массу вашего тела: "))
    height = float (input("Введите ваш рост в метрах: "))
    if height > 5:
        height /= 100
    result = is_normal(mass=mass, height=height)
    if result:
        print ("Ваш индекс массы тела находится в норме")
        print (f"Ваш личный специалист - {name_spec} - поможет вам в" + \
               "более эффективных тренировках")
        print (f"\nВаше индивидуальное время для консультации со специалистом: {time_for_consult}")
    else:
        print ("Ваш индекс массы тела вне нормы, но не переживайте!" +\
               f"\nНаш специалист - {name_spec} поможет вам не только исправить проблемы веса, но" +\
               " и помочь с тренировками'")
        print (f"\nВаше индивидуальное время для консультации со специалистом: {time_for_consult}")

