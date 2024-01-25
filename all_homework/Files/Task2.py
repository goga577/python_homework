"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
with open("mini_ginius.txt", "w+") as file:
    file.write("но у меня не получается")

old_file1 = open("genius.txt", "r")
old_str1 = old_file1.read()
old_file1.close()
old_file2 = open("mini_ginius.txt", "r")
old_str2 = old_file2.read()
old_file2.close()
new_file = open("multi_str", "w+")
new_file.write(old_str1 + ", " + old_str2)
new_file.seek(0)
print(new_file.read())
