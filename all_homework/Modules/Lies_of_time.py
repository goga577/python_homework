import random
def random_time (begin,finish, minutes : str = "00"):
    time_random = str(random.randint(begin, finish)) + ":" + minutes
    return time_random
def give_me_table () ->dict:
    no_job_time = "ВЫХОДНОЙ"
    section_list = ["Тенис", "Волейбол", "Йога", "Настольный теннис", "Занятия с личным тренером", "Бокс", "Курсы по здоровью", "СБ", "ВС"]
    table = {}
    for i in section_list:
        if i == "СБ" or i == "ВС":
            table [i] = no_job_time
        else:
            table [i] = (f"{random_time(9,10)} - {random_time(11,20)}")
    return table