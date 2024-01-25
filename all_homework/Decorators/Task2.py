"""
Напишите программу добавляющую в рецепт бутерброда ингридиенты "Салат" и "Ананасы" с помощью декораторов.
"""
def my_little_dec (func):
    def Wrapper():
        print ('Программа для рецептов бутербродов')
        func()
        print('А ещё добавьте ананас и салат - с ним всё лучше')
    return Wrapper
        
@my_little_dec
def my_brot ():
    list_recipe = []
    responce = input('Введите ингредиент: ')
    while responce != 'off':
        list_recipe.append(responce)
        responce = input('Введите ингредиент или (off для завершения): ')
    for i in list_recipe:
        print (i)
my_brot ()