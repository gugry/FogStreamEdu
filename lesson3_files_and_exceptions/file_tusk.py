# 3. Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.
# Выведите три найденных числа в формате, приведенном в примере.
# Пример входного файла:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Пример выходного файла:
# Input file contains:
# 108 letters
# 20 words
# 4 lines

import re

# Read input file.
income = str (input())
try:
    workin_file = open(income,'r')
except FileNotFoundError :
    print('Ошибка в имени файла. Использовано значение по умолчанию')
    workin_file = open('input_file.txt','r')
workin_content = workin_file.read()
workin_file.close()

#Count latin letters, words and lines
workin_latin = re.findall('[A-Za-z0]',workin_content)
latin_count = len(workin_latin)

workin_words = workin_content.replace('\n', ' ').split(' ')
words_count = len(workin_words)

workin_lines = workin_content.split('\n')
lines_count = len(workin_lines)

# Стоит ли оставлять подобные блоки кода для удобства тестирования при его поддержки?
# print('Количество латинских букв:', latin_count)
# print('Количество слов:', words_count)
# print('Количество строк:', lines_count)

# write in output file
workin_file = open('output_file.txt','w')
str_for_write = str(latin_count) + \
                ' letters\n' + \
                str(words_count) + \
                ' words\n' + \
                str(lines_count) + \
                ' lines\n'
workin_file.write(str_for_write)
workin_file.close()


