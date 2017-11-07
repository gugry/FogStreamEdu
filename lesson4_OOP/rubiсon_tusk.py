# 3.Дан файл с каким-то математическим выражением,
# которое содержит скобки разных типов “{[()]}” в любом порядке.
# Проверить сбалансированны ли скобки.
# В случае сбалансированности вывести результат вычисления выражения,
# иначе указать позицию скобки, которая нарушает баланс.

import re

def cheking_math(income_math):
    """"return position(s) of unbalanced brakets"""

    brackets = ['(', ')', '[', ']', '{', '}']

    # Перебераем выражение до тех пор, пока в нем есть скобки
    while re.search(r'[\)\]}\(\[{]', income_math):

        # Find first close braket. If nothing is found, return error.
        close_braket = re.search(r'[\)\]}]', income_math)
        if close_braket:
            position_close = close_braket.span()[0]
        else:
            return ([re.search(r'[\(\[{]', income_math).span()[0]])

        # Reverse find first open braket. If nothing is found, return error.
        open_braket = re.search(r'[\(\[{]', income_math[position_close::-1])
        if open_braket:
            position_open = len(income_math[position_close::-1]) - open_braket.span()[1]
        else:
            return ([position_close])

        # Check brakets the same tipe. If the same, replace them on "_". Otherwise return error.
        bracket_type = brackets.index(close_braket.group()) - 1
        if open_braket.span()[0] == income_math[position_close::-1].find(brackets[bracket_type]):
            income_math = '_'.join([income_math[:position_open:],
                                        income_math[position_open + 1:position_close:],
                                        income_math[position_close + 1::]])
        else:
            return ([position_open, position_close])

# Read input file.
income = str (input())
try:
    workin_file = open(income,'r')
except FileNotFoundError :
    print('File name error. The default value is used: input_file.txt')
    workin_file = open('input_file.txt','r')
workin_content = workin_file.read()
workin_file.close()

# Check for math
unmath_err = re.findall('[^\d+\-%*/\)\]}\(\[{]', workin_content)
if unmath_err:
    # easter egg
    if workin_content.upper() == 'HELLO WORLD':
        print('ПРИВЕЕЕЕТ =D')
    else:
        print('Error: Incoming expression can consist only of: ')
        print('numbers: 0-9')
        print('brakets: ()[]{}')
        print('mathematical operations: + - % *')
else:
    income_math = workin_content
    math_err = cheking_math(income_math)

    if math_err:
        print('error:', math_err)
    else:
        income_math = re.sub('[\[{]', '(', income_math)
        income_math = re.sub('[\]}]', ')', income_math)
        try:
            print(eval(income_math))
        except SyntaxError:
            print('Mathematical expression error!')
            workin_file = open('input_file.txt', 'r')

