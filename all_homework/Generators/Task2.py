
t = "Генератор – это итератор, элементы которого" +\
"можно перебирать (итерировать) только один раз. " +\
"Итератор – это объект, который поддерживает функцию next() " +\
'для перехода к следующему элементу коллекции."'

def my_generic(str_responce:list):
    for word in str_responce:
        yield word

def main(t:str):
    lazy_word = my_generic(t.split())
    for word in lazy_word:
        print(word)
main(t)