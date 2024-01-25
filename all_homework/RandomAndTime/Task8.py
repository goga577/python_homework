def is_magic_day (date:list):
    day = int(date[0])
    month = int(date[1])
    year_str = date[-1]
    last_num_year = int(year_str [-2] + year_str[-1]) #1960 - 1-0 9-1 6-2
    if month * day == last_num_year:
        return True
    else:
        return False

def main ():
    date_list = input("Введите дату через точку: ").split(".")
    responce = is_magic_day(date=date_list)
    if responce:
        print ("УРА! Сегодня магическая дата! Достаём мётлы и котлы!")
    else:
        print ("Эх, сегодня магия нас покинула...")
main()