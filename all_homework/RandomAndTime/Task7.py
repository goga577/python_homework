'''Номерной знак имеет вид Х000ХХ00
где Х – буква от А до Я, а 0 – цифра от 0 до 9. Напишите функцию генерирующую случайный номерной знак'''
import random
def give_me_num () ->str:  #Первое, что пришло в голову - сделать кучу циклов
    ready_num = []
    list_abc = "ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБА"
    ready_num.append(random.choice(list_abc))
    for i in range (3):
        ready_num.append(str(random.randint (1,9)))
    for i in range (2):
        ready_num.append(random.choice(list_abc))
    for i in range (2):
        ready_num.append(str(random.randint (1,9)))
    return "".join(ready_num) #Возвращаем строку

def give_me_num2() ->str: #Второе, что пришло в голову - конкатенация
    list_abc = "ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБА"[::-1]
    num1 = str(random.randint (1, 999))
    num2 = str(random.randint(1,99))
    ready_num = random.choice(list_abc) + num1 + random.choice(list_abc) + random.choice(list_abc) + num2
    return ready_num

def main ():
    print ("Ваш новый номер: ")
    print (f"{give_me_num2()}")

main()