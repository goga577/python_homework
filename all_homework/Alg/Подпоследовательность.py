def it_is_sres (str1 : str, str_search : str): #Подстрока = срез (?)
    start = str1.find(str_search)
    finish = str1.rfind(str_search)
    sres = finish - start
    return sres

def it_is_sres_2 (str1 : str, str_search : str):
    set1 = set(list(str1))
    set_search = set(list(str_search))
    final_num = set1 & set_search
    return final_num