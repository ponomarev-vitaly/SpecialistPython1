# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
first_number = int(input("Введите первое число: "))     # Первое число
second_number = int(input("Введите второе число: "))    # Второе число
for first_number in range (first_number,second_number):
    if first_number % 3 == 0:
        print(first_number)
