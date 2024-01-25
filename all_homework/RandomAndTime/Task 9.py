import random
import time
def go_coin():
    coin = ["Орёл", "Решка"]
    start = time.time()
    one_toss = random.choice(coin)
    print(one_toss)
    sec_toss = random.choice(coin)
    print(sec_toss)
    three_toss = random.choice(coin)
    print(three_toss)
    print(one_toss != sec_toss or sec_toss != three_toss or one_toss != three_toss) #Соблюдается ли
    #наше условие для запуска цикла
    while one_toss != sec_toss or sec_toss != three_toss or one_toss != three_toss:
        print("ЦИКЛ ЗАПУЩЕН! ")
        one_toss = random.choice(coin)
        print(one_toss)
        sec_toss = random.choice(coin)
        print(sec_toss)
        three_toss = random.choice(coin)
        print(three_toss)
    end = time.time()
    finish = end - start
    return finish

def main ():
    print ("Бросаем монету, пока все результаты не будут одинаковы")
    final = go_coin()
    print (f"Мы смогли получить нужные результат за: {final}")
main ()