"""
�������� ������ ������� �� ����������. ������������ ������ ���.
���� ��� ������������� �� �,�,�,�, �� ��������� ��������� � ����� "�����".
���� �� �,�,�,�. �� ����������� "����������". ���� �� �� ���� �� ���� ���� �� ����������� "������" ����� ������.
"""
genius = lambda name: "Гений " + name
genius_list = ['а', 'я', 'г', 'м']
overmind = lambda name: "Сверхразум " + name
overmind_list = ['о', 'ь', 'л', 'н']
it_is_fine = lambda name: "Просто " + name
name = input("Введите ваше имя: ")
if list(name.lower())[-1] in genius_list:
    print (genius(name))
elif list(name.lower())[-1] in overmind_list:
    print (overmind(name))
else:
    print (it_is_fine(name))