import random
import time
import Lies_of_trainer
def give_me_card():
    list_of_lie = [True, False]
    input("Введите ваше ФИО: ")
    input("Введите дату рождения: ")
    num_card = input("Введите номер карты: ")
    while len(num_card) != 16:
        print("Неверные данные карты.")
        num_card = input("Введите номер карты повторно: ")
    print("Делаем запрос в банк...")
    time.sleep (3)
    print("Для подтверждения транзакции введите код из SMS-сообщения")
    lie_SMS = random.randint (1123, 4221)
    SMS = input("Код из SMS: ")
    print ("Ожидаем подтвержения транзации...")
    time.sleep(3)
    if SMS == lie_SMS: #Угадай число от 1123 до 4221 (unreal)
        print ("ПОЗДРАВЛЯЕМ! Оплата прошла успешно!")
        return True
    else:
        print ("Ошибка оплаты")
        print ()
        print ("Пожалуйста, повторите попытку позже")
        return False

def why_pay ():
    print("Какой способ оплаты вы бы хотели использовать?" + \
          "\n1 - оплата картой" + \
          "\n2 - оплата при личном посещении")
    responce_price = int(input("Ваш ответ: "))
    result = True
    while responce_price == 1 and result == True:
        result = give_me_card()
        return result
    else:
        print("Для оплаты путём личного посещения вы моежет подойти " + \
              "с 12:00 до 16:20 во вторник, среду и пятницу к стойке регистрации")
        print(f"Номер телефона сотрудника для дополнительных справок: {Lies_of_trainer.give_me_phone()}")
        result = False
        return result