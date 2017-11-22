# 5. Создать класс для хранения комплексных чисел.
# Реализовать операции над комплексными числами:
# сложение, вычитание, умножение, деление, сопряжение, возведение в степень, извлечение корня.
# Предусмотреть возможность изменения формы записи комплексного числа:
# алгебраическая форма, тригонометрическая форма, экспоненциальная форма.
# http://www.mathforyou.net/online/numbers/complex/convert/

import math
import cmath

class Uncomplex_input_exception(Exception):
    '''Exception for uncomplex input keys'''

    def __init__(self):
        Exception.__init__(self)
        self.text = 'Error: Transmitted number is not complex'

class Complex_num():
    """ Keeps a complex number and tools for working on it
    complex_num: complex number value in numeric form
    form_type: form of complex_number
    modul and arg: module and argument of complex number in trigonometric
                                                    and exponential forms
    """

    def __init__(self, complex_num):
        try:
            if not (isinstance(complex_num, complex)):
                raise  Uncomplex_input_exception
            else:
                self.complex_num = complex_num
                self.form_type = 'algebraic'
                self.modul = abs(self.complex_num)
                self.arg = cmath.phase(self.complex_num)
        except Uncomplex_input_exception as ex:
            print(ex.text)

    def __call__(self, *args, **kwargs):
        if self.form_type != 'algebraic':
            return [self.modul, self.arg]

        else:
            return self.complex_num

    def grade_algebraic(self):
        """upgrade complex_num for keys trigonometric
                    or exponential forms changed keys
        """

        self.complex_num = complex(self.modul * math.cos(self.arg),
                                   self.modul * math.sin(self.arg))

    def grade_exponential(self):
        """upgrade modul and arg for algebraic exponential form changed keys"""

        self.modul = abs(self.complex_num)
        self.arg = cmath.phase(self.complex_num)

    def summation(self, term):
        """adds term for complex number"""

        self.complex_num += term
        self.grade_exponential()

    def subtraction(self, term):
        """subtracts term from complex number"""

        self.complex_num -= term
        self.grade_exponential()

    def multiplication(self, term):
        """multiplies term on complex number"""

        self.complex_num *= term
        self.grade_exponential()

    def division(self, term):
        """divides complex number on term"""
        if term == 1:
            return 'Error: term should not be equal'
        else:
            self.complex_num /= term
            self.grade_exponential()

    def exponentiation(self, term):
        """raises complex number to the power of term"""

        self.complex_num **= term
        self.grade_exponential()

    def sqrt(self, degree):
        """return a root complex number
        degree: degree of the root
        """
        result = []
        for count in range(degree):
            result.append([self.modul * (math.cos((self.arg + 2 * math.pi * count) / degree)),
                            self.modul * (math.sin((self.arg + 2 * math.pi * count) / degree))])
        return result

    def turn_to_algebraic(self):
        """turn form of complex number on algebraic"""

        self.form_type = 'algebraic'
        self.grade_algebraic()

    def turn_to_trigonometric(self):
        """turn form of complex number on trigonometric"""

        self.form_type = 'trigonometric'
        self.grade_exponential()

    def turn_to_exponential(self):
        """turn form of complex number on exponential"""

        self.form_type = 'exponential'
        self.grade_exponential()

    def what_form(self):
        """return current form of complex number"""

        return self.form_type
