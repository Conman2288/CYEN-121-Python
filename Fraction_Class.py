# Fracton class
# STATE
# --- numerator
# --- denominator
# Behavior
# --- addition
# --- subtraction
# --- rewrite as mixed number
# --- reduce / simplify
# --- multiply
# --- divide

class Fraction:
    def __init__(self, num = 0, den = 1):
        self.num = num
        if (den == 0):
            den = 1
        self.den = den

    @property
    def num(self):
        return self._num

    @property
    def den(self):
        return self._den

    @num.setter
    def num(self, value):
        self._num = value

    @den.setter
    def den(self, value):
        if (value != 0):
            self._den = value

    def get_real(self):
        return float(self.num) / self.den
    def reduce(self):
        gcd = 1
        minimum = min(abs(self.num), abs(self.den))

        # find common divisors
        for i in range (2, int(minimum + 1)):
            if (self.num % i == 0 and self.den % i == 0):
                gcd = i

        # divide the numerator and the denominator by the GCD
        self.num /= gcd
        self.den /= gcd

        # if the numerator is 0, set denominator to 1
        if (self.num == 0):
            self.den = 1

    def __add__(self, other):
        num = (self.num * other.den) + (self.den * other.num)
        den = self.den * other.den
        sum = Fraction(num, den)
        sum.reduce()
        return sum

    def __sub__(self, other):
        num = (self.num * other.den) - (self.den * other.num)
        den = self.den * other.den
        diff = Fraction(num, den)
        diff.reduce()
        return diff

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        product = Fraction(num, den)
        product.reduce()
        return product

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        div = Fraction(num, den)
        div.reduce()
        return div
    
    def __str__(self):
        self.reduce()
        return ("{}/{}  ({})".format(self.num, self.den, self.get_real()))



f1 = Fraction(3, 12)
print(f1)
f2 = Fraction(5, 7)
print(f2)
f3 = f1 + f2
print(f3)
f4 = f1 - f2
print(f4)
f5 = f1 * f2
print(f5)
f6 = f1 / f2
print(f6)


