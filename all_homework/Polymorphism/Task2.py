"""
Создать базовый класс ОЛИМПИАДНЫЕ ЗАДАНИЯ (данные об участнике, количество тестовых примеров,
количество пройденных тестов).
Создать производные классы ЗАДАНИЯ «ВСЕ ИЛИ НИЧЕГО»
(задается максимальное количество баллов за задание (даются только когда все тесты пройдены)
и ЗАДАНИЯ «ЧЕМ БЫСТРЕЕ, ТЕМ ЛУЧШЕ» (задается время участника на решение,
лучшее время всех участников, максимальное количество баллов за задание,
процент снижения балла в минуту отставания от лучшего времени).
Для заданных примеров задач, которые решали участники,
упорядочить участников по росту набранных баллов и определить суммарное количество баллов,
набранных заданным участником олимпиады.
Для проверки использовать действия над списком,
в котором разместить объекты разных производных классов.
"""
class Olimpic_quastion:
    def __init__(self,name,num_quastion, num_test):
        self.name = name
        self.num_quastion = num_quastion
        self.num_test = 'all'
class All_or_Nothing(Olimpic_quastion):
    def __init__(self, name,num_quastion,num_test,max_ball):
        super().__init__(name,num_quastion,num_test)
        self.max_ball = 0
        if self.num_test == 'all':
            self.max_ball = max_ball
class Speed_qustion(Olimpic_quastion):
    def __init__(self,name,num_quastion,num_test, time_for_ready, procent):
        super().__init__(name,num_quastion,num_test)
        self.time = time_for_ready
        self.procent = procent
