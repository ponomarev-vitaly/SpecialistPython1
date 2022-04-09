# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

print(', '.join(map(str, names)))
print (f"{names[0]}, {names[1]}, {names[2]}, {names[3]}, {names[4]}")
[print(name, end=", ") for name in names]

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
