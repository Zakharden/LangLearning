"""Проверяет, счастливое ли число"""
ticket_number = int(input("Введите номер билета: "))
sum_chet = 0
sum_nechet = 0
if len(str(ticket_number))<6:
    print("Номер билета должен состоять из 6 чисел!")
    ticket_number = int(input("Внимательно введите номер билета: "))
else:
    while ticket_number>0:
        sum_chet+=ticket_number%10
        sum_nechet+=(ticket_number%100)//10
        ticket_number=ticket_number//100
if sum_chet==sum_nechet:
    print("Счастливый билет 😏")
else:
    print("Несчастливый билет ☹️")