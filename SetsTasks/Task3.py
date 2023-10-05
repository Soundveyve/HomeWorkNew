"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Даны списки семей в квартирах.
Используя операции со множествами вычислите сколько семей живёт в доме N.
"""
newspaper = set(range(1, 76))
magazine = set (range(77, 104))
both = set(range(21, 34))
newspaper_magazine = newspaper | magazine #Сложили 2 множества
all_family = list(newspaper_magazine | both) #Сложили результат 1 сложения с 3 множеством и
#перевели всё в список (т.к всё получено из множества, то элементы уникальны)
print (f"Всего семей в доме: {all_family[-1]}") #Выводим последний элемент из списка 