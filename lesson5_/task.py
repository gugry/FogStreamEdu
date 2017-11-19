# 5. Создать класс для хранения комплексных чисел.
# Реализовать операции над комплексными числами:
# сложение, вычитание, умножение, деление, сопряжение, возведение в степень, извлечение корня.
# Предусмотреть возможность изменения формы записи комплексного числа:
# алгебраическая форма, тригонометрическая форма, экспоненциальная форма.
# http://www.mathforyou.net/online/numbers/complex/convert/
import math
import cmath
class Complex_num():
    def __init__(self,complex_num):
        if not (isinstance(complex_num, complex)):
            print('Error: Transmitted number is not complex')
        self.complex_num = complex_num
        self.form_type = 'algebraic'
        self.modul = abs(self.complex_num)
        self.arg = cmath.phase(self.complex_num)

    def __call__(self, *args, **kwargs):
        if self.form_type != 'algebraic':
            return [self.modul, self.arg]

        else:
            return self.complex_num


    def summation(self,term):
        self.complex_num += term

    def subtraction(self,term):
        self.complex_num -= term

    def multiplication (self,term):
        self.complex_num *= term

    def division(self,term):
        self.complex_num /= term

    def exponentiation(self,term):
        self.complex_num **= term

    def grade_algebraic(self):
        self.complex_num = complex(self.modul*math.cos(self.arg),
                                   self.modul*math.sin(self.arg))
    def grade_exponential(self):
        self.modul = abs(self.complex_num)
        self.arg = cmath.phase(self.complex_num)

    def sqrt(self,degree):
        result=[]
        for count in range(degree):
            result.append([self.modul * (math.cos((self.arg + 2 * math.pi * count) / degree)),
                           self.modul * (math.sin((self.arg + 2 * math.pi * count) / degree))])
        return result

    def turn_to_algebraic(self):
        self.form_type = 'algebraic'
        self.grade_algebraic()


    def turn_to_trigonometric(self):
        self.form_type = 'trigonometric'
        self.grade_exponential()

    def turn_to_exponential(self):
        self.form_type = 'exponential'
        self.grade_exponential()

#test comment
