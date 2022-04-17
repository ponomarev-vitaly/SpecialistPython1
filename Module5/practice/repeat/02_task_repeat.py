# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    pass

number = int(input("Print the number: "))
res = 0
copy_number = number
while number != 0:
    digit = number % 10
    res = res * 10 + digit
    number = int(number / 10)

if res == copy_number:
    print("Palindrome")
else:
    print("Not a palindrome")
