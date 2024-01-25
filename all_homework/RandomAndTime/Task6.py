#1.	Напишите функцию для генерации случайного пароля состоящего из цифр, букв и спецсимволов.
#Функция должна принимать 1 аргумент – желаемую длину пароля и генерировать пароль данной длинны
import random
def give_me_password2(n):
    str_passw = "1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*"
    password = []
    for i in range(n):
        password.append(random.choice(str_passw))
    return "".join(password)

def main ():
    num_passw = int(input("Введите длину вашего пароля: "))
    password = give_me_password2(num_passw)
    print (f"Ваш пароль : {password}")

main ()