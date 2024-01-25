"""
Напишите генератор выводящий все числа делящиеся на 11 в диапазоне от 0 до 100
"""
def main():
    number_generic = (i for i in range(101) if i % 11 == 0 and i != 0)
    for number_from_generic in number_generic:
        print(number_from_generic)
main()