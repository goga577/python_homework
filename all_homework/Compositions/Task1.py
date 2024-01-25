"""
Создайте композицию User состояющую из:
Объекта Profile со свойствами: name,last_name,age,pasport и методом print_info.
Объекта Address со свойствами : City,street,zipcode
Объекта Role со свойствами: role,hours_worked
Объекта BankAccount со свойствами: card_number, balance
Объекта Order с методом устанавливающими параметры заказа: Item,date,delivery,price
Добавьте в композицию методы создания профиля, установки адреса, роли, привязки банковского аккаунта и добавления заказа
"""
class Profile:
    def __init__(self, name, last_name, pasport): #Окей
        self.name = name
        self.last_name = last_name
        self.pasport = pasport
    def print_info(self):
        print(f'Имя: {self.name}'
              f'\nФамилия: {self.last_name}'
              f'\nНомер паспорта: {self.pasport}')
class Address:
    def __init__(self, city, street, zipcode):
        self.city = city
        self.street = street
        self.zipcode = zipcode
class Role:
    def __init__(self, role, hours_worked):
        self.role = role
        self.hours_worked = hours_worked
class BankAccount:
    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance
class Order:
    def __init__(self, item,date, delivery, price):
        self.item = item
        self.date = date
        self.delivery = delivery
        self.price = price
class User:
    def __init__(self):
        self.profile = 'нет профиля'
        self.addres_list = []
        self.role_list = []
        self.bank_acc_list = []
        self.order_list = []
    def create_profile(self, name, pasport, last_name):
        self.profile = Profile(name=name, last_name=last_name, pasport=pasport) #Не помню последовательность, поэтому не позиционно
    def add_address(self, city, street, zipcode):
        self.addres_list.append(Address(city, street, zipcode))
    def add_role(self, role, hours_worked):
        self.role_list.append(Role(role,hours_worked))
    def add_bank_account(self, card_number, balance):
        self.bank_acc_list.append(BankAccount(card_number, balance))
    def add_order(self, item, date, delivery, price):
        self.order_list.append(Order(item, date, delivery, price))

Andrey = User()
menu = ('1 - Добавить профиль'
        '\n2 - Добавить адрес'
        '\n3 - Добавить роль'
        '\n4 - Добавить банковский аккаунт'
        '\n5 - Далее (в никуда)')
print(menu)
responce = int(input('Введите желаемое действие: '))
while responce != 5:
    if responce==1:
        name = input('Введите имя: ')
        last_name = input('Введите фамилию: ')
        pasport = int(input('Введите серию паспорта'))
        Andrey.create_profile(name=name, last_name=last_name,pasport=pasport)
        print (f'Ура, пользователь с именем {Andrey.profile.name}')
    if responce == 2:
        city = input('Введите название вашего города: ')
        street = input('Введите вашу улицу: ')
        zipcode = int(input('Введите ваш индекс: '))
        Andrey.add_address(city, street, zipcode)
        print (f'Ура, вы добавили новый адрес')
    if responce == 3: #
        role = input('Введите роль на добалвение: ')
        hours = int(input(f'Введите количество часов для роли "{role}": '))
        Andrey.add_role(role, hours)
    if responce == 4:
        pass