"""
Напишите программу-имитатор подбрасывания 2 кубиков.
Программа выводит на экран "подбрасываю кубики" и спустя 2 секунды выводит значения на кубиках в одну строку.
"""
import random
import time
from random import randint
from time import sleep
def cobe ():
    responce = "да"
    yes_list = ["yes", "да"]
    while responce in yes_list:
        toss1 = random.randint(1, 6)
        toss2 = random.randint(1, 6)
        print("ПОДБРАСЫВАЮ КУБИКИ!")
        time.sleep(2)
        print(toss1, toss2)
        print("Нужно ли вновь бросить кубики?")
        responce = input("Ваш ответ: ").lower()
def main ():
    cobe()
    print ("Переместите фигурки Кархарадонов!")
main ()
