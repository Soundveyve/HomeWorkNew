"""
Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.
Программа должна запрашивать количество набранных баллов и печатать сообщение «Ваша скидка:» и скидку:
— от 0 до 49 баллов — «Скидка 10%»;
— от 50 до 99 баллов — «Скидка 15%»;
— от 100 баллов и выше — «Скидка 20%».

Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
"""
def give_me_procent (ball:int):
    if ball > 0 and ball <= 49:
        procent = 10
    elif ball >= 50 and ball <= 99:
        procent = 15
    elif ball >= 100:
        procent = 20
    else:
        procent = 0
    return procent
ball = int (input("Введите количество ваших баллов: "))
procent_sale = give_me_procent(ball)
if procent_sale > 0:
    print (f"ПОЗДРАВЛЯЕМ! Ваша скидка: {procent_sale}")
else:
    print ("Вы ещё не купили билеты, обратитесь на кассу")