"""
Напишите программу которая будет спрашивать пользователя ввод имени пока пользователь не введет off.
Программа должна используя lambda-функцию добавлять к каждому имени надпись "гений".
"""

name = input("Введите имя: ")
while name.lower() != 'off':
    genius_name = lambda name: name + " гений"
    print(genius_name(name))
    name = input("Введите имя: ")