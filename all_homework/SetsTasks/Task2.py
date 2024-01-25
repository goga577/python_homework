"""
Имеется список с произвольными значениями. Нужно преобразовать его во множество и проверить
являются ли все его элементы неизменяемыми.
Вывести True или False. И изменяемые элементы
Подсказка: чтобы узнать тип элемента можно использовать функцию type()
"""
testList = [1,2,2,[3,4],(1,2,3),"1",{1,2,3}]
printSet = set()
list_edit = []
for i in testList:
    if type(i) == set or type(i) == list or type(i) == dict:
        list_edit.append(i)
        print (i)
        print(False)
    else:
        print (i)
        print(True)
        printSet.add(i)
print (f"Изменяемые элементы, которые не были включены во множество: {list_edit}")
print (f"Множество из изменяемых элементов: {printSet}") #s