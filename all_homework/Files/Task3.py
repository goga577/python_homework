"""
Напишите программу, которая будет считывать содержимое файла, добавлять к считанным строкам порядковый номер и сохранять их в таком
виде в новом файле. Имя исходного файла необходимо запросить у пользователя, так же, как и имя целевого файла. Каждая строка в созданном
файле должна начинаться с ее номера, двоеточия и пробела, после чего
должен идти текст строки из исходного файла.
"""
file_for_read = open("FileforTask3.txt", "r") #Правильное ли решение?
file_for_write = open("Number_stroke.txt", "w+")
num_stroke = 0
for stroke in file_for_read:
    file_for_write.write(f"{num_stroke}: " + stroke)
    num_stroke += 1
file_for_write.close()
file_for_read.close()