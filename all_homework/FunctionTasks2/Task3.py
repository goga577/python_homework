"""
Напишите программу, которая будет складывать числа, введенные поль-
зователем. Сигналом к окончанию ввода должна служить пустая строка.
Отобразите на экране сумму значений (или 0.0, если пользователь сразу
же пропустил ввод). Решите эту задачу с использованием рекурсии. В ва-
шей программе не должны присутствовать циклы.
Подсказка. В теле вашей рекурсивной функции должен производиться запрос одно-
го числа у пользователя, после чего должно быть принято решение о том, произво-
дить ли еще один рекурсивный вызов. Ваша функция не должна принимать аргумен-
тов, а возвращать будет числовое значе
"""
sum1 = 0
def get_sum ():
    n = float(input("Введите число для складывания: "))
    if n != 0:
        global sum1 = sum1 + n
        return n + get_sum()
    else:
        print (sum1)
        return 0

get_sum()