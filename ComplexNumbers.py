"""
Add = Addition of each component
"""


class ComplexNumber:
    def __init__(self, A=0, B=0):
        self.A = A
        self.B = B

    def __add__(self, other):
        comp = ComplexNumber(self.A + other.A,  self.B + other.B)
        return comp

    def __mul__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __idiv__(self, other):
        comp = ComplexNumber(self.A / other.A)
        return comp


c = ComplexNumber()
d = ComplexNumber(1, 2)
c.__add__(d)
