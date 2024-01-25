def euclid (m, n):
    r = m % n
    while r > 0:
        m = n
        n = r
        r = m % n
    print (n)
    return n

def extended_euclidus (a,b):
    if a == 0:
        return b, 0, 1
    nod, x1, y1 = extended_euclidus(b % a, a)
    x = y1 - b // a * x1
    y = x1
    return nod, x, y

def IsPrime(n): #
    if n < 2:
        return False
    for i in range (2, int (n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def eratosthenes (n):
    list_num = list(range (2, n))
    for i in range (len (list_num)):
        if list_num[i] != 0:
            p = list_num [i]
            for j in range (2*p-2, len(list_num), p):
                list_num [j] = 0
    list_fi_num = [i for i in list_num if i > 0]

#Выучить все алгоритмы, кроме расширенного алгоритма Эвклида