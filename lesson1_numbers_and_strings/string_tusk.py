#5.Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.
input_str = input()
new_str = input_str[0:3];
for i in range(4,len(input_str), 3):
    new_str = new_str + input_str[i:i+2]
print (new_str)
