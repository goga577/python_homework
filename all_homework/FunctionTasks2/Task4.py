"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""
def coluluate (*arg):
    average = sum(arg) / len(arg)
    up_average = [i for i in arg if i > average]
    return (average,up_average)
my_result = coluluate(1,23,41,124,5,6,7,4,16,100,73,87,42,52,33)
print(f"Среднее значение параметров: {my_result[0]:.2f}")
print(f"Числа выше среднего значения: {my_result[1]}")