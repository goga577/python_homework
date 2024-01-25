"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""
def set_group (name:str, group:int, new_group:int):
    if name != None and group!= None and new_group != None:
        print (f"{name}, ваша старая группа: 0{group}")
        print (f"Ваша новая группа: 0{new_group}")
    else:
        print(f"Повторите отправку данных ")

set_group(name="Борис", new_group= 611, group=711)