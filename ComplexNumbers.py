"""
    Add = Addition of each component
"""


class ComplexNumber:
    def __init__(self, A=0, B=0):
        self.A = A
        self.B = B

    def __add__(self, other):
        return ComplexNumber(self.A + other.A,  self.B + other.B)

    def __mul__(self, other):
        return ComplexNumber(self.A)

    def __sub__(self, other):
         ComplexNumber(self.A - other.A,  self.B - other.B)

    def __idiv__(self, other):
        return ComplexNumber(self.A / other.A)

