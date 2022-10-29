import time

# a = int(input("Введите число : "))
#
# result = a ** 2
# print(f"{a} ^ 2 = {result}")

# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} * {b} = {a*b}")
# print(f"{a} ^ {b} = {a**b}")
# print(f"{a} / {b} = {a/b}")
# print(f"{a} // {b} = {a//b}")
# print(f"{a} % {b} = {a%b}")

# Ctrl + /   - Комментирование
#
# if a > b :
#     print("A больше B")
# elif b > a :
#     print("B больше A")
# else:
#     print("Они равны")



a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
command = input("Введите команду: ")

while command != "STOP":
    if command == "+":
        print(f"{a} + {b} = {a+b}")
    elif command == "-":
        print(f"{a} - {b} = {a-b}")
    elif command == "*":
        print(f"{a} * {b} = {a * b}")
    elif command == "^":
        print(f"{a} ^ {b} = {a ** b}")
    elif command == "/":
        print(f"{a} / {b} = {a / b}")
    elif command == "show":
        print(f"a = {a}")
        print(f"b = {b}")
    elif command == "update":
        a = int(input("Введите новое число A: "))
        b = int(input("Введите новое число B: "))
    else:
        print("Такой команды не найдено")
    command = input("Введите новую команду: ")

print("Конец работы калькулятора")





#
# seconds = 1
# minutes = 0
#
# while minutes != 2 :
#     time.sleep(1)
#     if seconds > 59:
#         seconds = seconds - 60
#         minutes = minutes + 1
#     if seconds > 9:
#         print(f"\t\t\t00:0{minutes}:{seconds}")
#     else:
#         print(f"\t\t\t00:0{minutes}:0{seconds}")
#     seconds = seconds + 1
#
# print("Конец")


# if text == "ПЛЮС":
#     print(f"{a} + {b} = {a+b}")
# elif text == "МИНУС":
#     print(f"{a} - {b} = {a-b}")
# elif text == "УМНОЖИТЬ":
#     print(f"{a} * {b} = {a * b}")
# else:
#     print("Такой команды не найдено")