"""
Напишите программу определяющую допуск ученика к зачету.
Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).

Ученикам без допуска должно печататься "Вы отчислены".

Выдачу допуска реализуй как функцию.
"""
def admission (students):
    for i in students:
        ball = int(input(f"Введите балл {i+1} ученика"))
        if ball < 50:
            print ("ПОЗДРАВЛЯЕМ! ВЫ УЧИТЕСЬ В НОВОМ МЕСТ...НО НЕ ЗДЕСЬ")

students = int(input("Введите количество учеников: "))
