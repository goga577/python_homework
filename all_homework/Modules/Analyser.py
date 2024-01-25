import Lies_of_pay
import Lies_of_trainer
import Lies_of_time
import Lies_of_surprise
import Lies_of_diet
import Lies_of_place
def Analyser_responce (responce:str):
    responce = set(responce.lower().split())  #Редакционное расстояние - оч сложна, самое лучшее - самое простое
    #Поэтому мы делаем всё через пересечения множеств
    list_timetable = ["расписание", "расписании","расп","расписания", "время", "секция", "секции", "секцию"]
    list_trainer = ["тренер", "тренера", "тренеры", "тренеры","работает", "телефон", "контакт"]
    list_price = ["сумма","оплата", "цена", "заплатить", "оплатить", "сколько", "денег"]
    list_surprise_ticket = ["абонемент", "подарок", "сюрприз", "именной", "сертификат"]
    list_diet = ["диету","врач","консультация", "диета", "врача", "диетолог", "диетолога"]
    list_city = ["филиалы", "города", "город", "филиал", "локации"]

    if responce & set(list_timetable):
        print ("Информация по расписанию: ")
        print ("Время работы зала: ПН-ПТ с 9:00 - 20:00")
        print ("Время секционных занятий: ")
        table = Lies_of_time.give_me_table()
        for section, time_section in table.items(): #Распаковываем
            print (f"{section} - {time_section}")

    elif responce & set(list_trainer):
        print ("Информация по контактным данным тренеров: ")
        dict_trainer = Lies_of_trainer.give_me_trainer()
        for phone, trainer in dict_trainer.items():
            print (f"{phone} - {trainer}")

    elif responce & set(list_price):
        Lies_of_pay.why_pay()
        print ("Приятного дня!")

    elif responce & set(list_surprise_ticket):
        Lies_of_surprise.give_me_ticket()

    elif responce & set(list_diet):
        Lies_of_diet.give_me_consultation()

    elif responce & {"иное", "другое", "подробно"}:
        print (f"По иным вопросам (или для уточнения) обращайтесь по номеру:" 
        f"\n{Lies_of_trainer.give_me_phone()}({Lies_of_trainer.give_me_name()})")
        print (f"Или очно по адресу: {Lies_of_place.give_me_lie_city()} - {Lies_of_place.give_me_lie_strasse()}")

    elif responce & set(list_city):
        dict_of_city = Lies_of_place.lie_full_place()
        for city in dict_of_city:
            print (f"{city} - {dict_of_city[city]}")

#Подарочный абонемент
#Консультация у диетолога
#Филиалы в других городах (ДЕДЛАЙН)