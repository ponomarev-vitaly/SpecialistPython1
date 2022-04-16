# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here
    lucky_ticket = [4, 3, 6, 7, 5, 1]


def ticket_finder():
    summa1 = sum(lucky_ticket[:3])
    summa2 = sum(lucky_ticket[:-3])
    if summa1 == summa2:
        return True
    else:
        return False


print("Is your tisket lucky?", ticket_finder())


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
