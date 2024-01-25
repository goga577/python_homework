"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def give_IMT ():
    height = float(input("Введите ваш рост: "))
    mass = float(input("Введите вашу массу: "))
    imt = mass / (height * height)
    return imt
def normal_IMT (imt):
    if imt >= 18.5 and imt <= 25:
        print (f"Ваш индекс массы тела {imt} в норме")
    elif imt > 25:
        print (f"Избыточный вес")
    else:
        print (f"У вас недостаток веса")

imt = give_IMT()
normal_IMT(imt)