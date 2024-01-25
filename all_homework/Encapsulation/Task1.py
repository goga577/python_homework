"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по password'у).
"""
class Account:
    def __init__(self, name, balance, password, pasport):
        self._name = name
        self.__password = password
        self.__balance = balance
        self.__pasport = pasport
    def get_me_pasport(self):
        return self.__pasport
    def get_me_balance(self):
        return self.__balance
    def i_do_not_mind_pasport(self, password, new_pasport):
        if password == self.__password:
            self.__pasport = new_pasport
            print('Пароль успешно измененён!')
        else:
            print ('ВЕРНИТЕ КАРТУ НА МЕСТО И НЕ ТРОГАЙТЕ ЕЁ!!!')
    def change_balance(self, summa):
        if self.__balance + summa < 0:
            print(f'Ваш баланс составляет {self.__balance} и указанная сумма - {-1 * summa} - не может быть снята')
        else:
            self.__balance = self.__balance + summa
            print(f'Баланс успешно изменён! Теперь баланс составляет {self.__balance}')
    def def_my_pasport(self,password):
        if password == self.__password:
            self.__pasport = None

