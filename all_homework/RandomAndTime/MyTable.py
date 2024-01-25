def give_me_table_multiplication():
    print("\tТаблица умножения")
    print("-" * 24)
    print("Номер\tУмножение")
    s = 1
    for i in range(1, 11):
        if s != 11: #Считаем номер
            for j in range(1, 11): #Сколько 1 * 1, 1 * 2 и т.д
                print(f"{s}\t\t{i} * {j} = {i * j}")
                s += 1
        else:
            s = 1
            print ()
            for j in range(1, 11): #Сколько 1 * 1, 1 * 2 и т.д
                print(f"{s}\t\t{i} * {j} = {i * j}")
                s += 1


give_me_table_multiplication()