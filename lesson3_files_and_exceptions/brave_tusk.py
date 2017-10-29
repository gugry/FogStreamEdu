# Написать консольную утилиту, передав которой путь к какой то папке,
# она выводит список файлов и папок, которые есть в этой папке.
# Используя библиотеки os и sys

#!/usr/bin/env python3
import os

print('Введите путь к папке')
income = str (input())
try:
    list_of_dir = os.listdir(path="income")
except FileNotFoundError:
    print('Ошибка ввода, использована текущая папка')
    list_of_dir = os.listdir(path="/")
print(list_of_dir)
for context in list_of_dir:
    print(context)

