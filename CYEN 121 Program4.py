############################################################################
# name: Connor Heard   
# date: 1 / 4 / 2023
# description: Program 4 - Complex Numbers
###########################################################################

# Don't forget to name this file Complex.py and place it in the same
# folder as the provided ComplexTest.py file so that they can
# automatically find and use each other.

class Complex:
    # A constructor that takes two values for the real and imaginary
        # portions respectively. Default values for both parameters are 0.
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

    # Accessors and Mutators for the instance variables
    @property
    def real(self):
        return self._real

    @property
    def imag(self):
        return self._imag

    @real.setter
    def real(self, value):
        self._real = value

    @imag.setter
    def imag(self, value):
        self._imag = value

    # Overloaded mathematical operators i.e. ==, +, -, *, /
    def __add__(self, other):
        sum_real = self.real + other.real
        sum_imag = self.imag + other.imag
        complex_sum = Complex(sum_real, sum_imag)
        return complex_sum

    def __sub__(self, other):
        diff_real = self.real - other.real
        diff_imag = self.imag - other.imag
        complex_diff = Complex(diff_real, diff_imag)
        return complex_diff

    def __mul__(self, other):
        prod_real = (self.real * other.real - self.imag * other.imag)
        prod_imag = (self.real * other.imag + self.imag * other.real)
        complex_prod = Complex(prod_real, prod_imag)
        return complex_prod

    def __truediv__(self, other):
         quot_real = (self.real * other.real + self.imag * other.imag) / (self.real **2 + self.imag **2)
         quot_imag = (self.real * other.imag - self.imag * other.real) / (self.real **2 + self.imag **2)
         complex_quot = Complex(quot_real, quot_imag)
         return complex_quot

    def  __eq__(self, other):
        if (self.real == other.real and self.imag == other.imag):
            return True
        else:
            return False      

    # Other functions e.g. reciprocal, conjugate, and __str__
    def reciprocal(self):
        recip_real = (self.real) / (self.real **2 + self.imag **2)
        recip_imag = -abs((self.imag) / (self.real **2 + self.imag **2))
        reciprocal_complex = Complex(recip_real, recip_imag)
        return reciprocal_complex

    def conjugate(self):
        conj_real = self.real
        conj_imag = -abs(self.imag)
        complex_conj = Complex(conj_real, conj_imag)
        return complex_conj

    def __str__(self):
        if (self.imag >= 0):
            return ("{} + {}i".format(self.real, self.imag))
        else:
            imaginary = abs(self.imag)
            return ("{} - {}i".format(self.real, imaginary))        
