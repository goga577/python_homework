import random
import Lies_of_pay
def give_me_ticket ():
    sur_name,name,paternity = input("Введите ФИО человека, на которого оформляется карта: ").split()
    number_of_ticket = random.randint (178276, 422100)
    print (f"Владелец абонемента: {sur_name} {name} {paternity}" +\
           f"\nНомер абонемента: {number_of_ticket}")
    print ("Завершите оформление сезонного абонемента его оплатой")
    print ()
    result = Lies_of_pay.why_pay()
    if result:
        print("Поздравляем с приобритением нашего прекрасного абонемента! ")