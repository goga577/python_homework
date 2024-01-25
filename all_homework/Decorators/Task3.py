"""
Напишите функцию которая принимает 2 числа и выводит все числа между ними которые делятся на 3.
Напишите декоратор который выводит фразу:
"Данная функция выводит все числа между Число А и Число Б"(сюда подставьте числа что принимает функция)
и оберните функцию чтобы данная фраза выводилась перед ее выполнением
"""
def decor (func):
    def Wrapper (start,finish):
        print (f'Данная функция выводит все числа между {start} и {finish}, которые деляться на 3')
        func (start,finish)
    return Wrapper

@decor
def my_number_func (start,finish):
    result = [i for i in range (start, finish + 1) if i % 3 == 0]
    print (result)

def main ():
    num_start = int(input('Введите первое число: '))
    num_finish = int(input('Введите второе число: '))
    if num_start > num_finish:
        num_finish, num_start = num_start, num_finish #Правильно определяем начальное и конечное число
    my_number_func (start = num_start, finish = num_finish)

main ()
    