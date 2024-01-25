"""
Напишите генераторное выражения. Для генерации словаря где ключем выступают числа от 0 до 10. А значения эти же числа в 16чной системе счисления.
Работу с 16чной системой найдите в документации Python
"""
def main ():
    my_generic_dict = {key:hex(key) for key in range(10)}
    for key_1,number_hex in my_generic_dict.items():
        print(key_1, "->", number_hex)
    print()
    my_list_generic = [i for i in range(10)]
    for any_one in my_list_generic:
        print(any_one)
main ()
#A = ((Z and B) or C) - расскажите, какое значение примет A, если Z неверно