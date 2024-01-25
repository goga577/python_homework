import time
def decor(func):
    def Wrapper ():
        start = time.time()
        print('УРА! Мы начали выполнять нашу чудесную функцию')
        func ()
        end =time.time ()
        print('Ура! Мы закончили выполнение нашей чудесной функции')
        finish = end - start
        print(f'Наша функция выполнилась за: {finish} сек')
    return Wrapper
@decor
def func_to_decor():
    for i in range(1000):
        print(i)
func_to_decor()