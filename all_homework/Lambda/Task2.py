"""
Функций sorted принимает в качестве дополнительного параметра key(Можете почитать документацию).
С помощью lambda-функции отсортируйте этот список словарей по именам
"""
grades = [{'name': 'Jennifer', 'final': 95},
     {'name': 'David', 'final': 92},
    {'name': 'Aaron', 'final': 98}]
result = sorted(grades, key=lambda x: x['name']) #Sorted принимает lambda-функцию к каждому элементу списка
#т.е sorted запрашивает у списка элемент, после этого элемент передаётся в lambda функцию
#далее уже lambda 'разворачивает' наш элемент как словрь
print (result)