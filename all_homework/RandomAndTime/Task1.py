"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""
import time
def give_me_time ():
    start = time.time()
    move = input("Введите ваш ход: ")
    if move != "off" and start != start/60:
        ready = time.time()
        final_time = ready - start
        print (f"Оставшееся время: {30 - final_time/60:.2f} минут")
def give_me_time2 ():
    game_time = 1800
    while game_time > 0:
        start = time.time()
        move = input("Введите ваш ход: ")
        end = time
        game_time -= end - start
        if move == "off":
            break
        print(f"У вас осталось: {game_time}")
    print("ИГРА ОКОНЧЕНА!")
give_me_time()
