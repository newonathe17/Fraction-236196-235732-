class Fraction():

    def __init__(self, numerator=0, denominator=1):

        if isinstance(numerator, str):
            numerator, denominator = numerator.strip().split('/')
            numerator = int(numerator)
            denominator = int(denominator)
        
        elif not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Numerator and denominator must be integers")
        
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        
        if denominator is None:
            denominator = 1

        greatest_common_divisor = self.gcd(abs(numerator), abs(denominator))

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        self.numerator = numerator // greatest_common_divisor
        self.denominator = denominator // greatest_common_divisor

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def get_numerator(self):
        return str(self.numerator)

    def get_denominator(self):
        return str(self.denominator)

    def get_fraction(self):
        if self.denominator == 1:
            return str(self.numerator)
        
        return f"{self.numerator}/{self.denominator}"

# Test cases
frac1 = Fraction(5, 1)
print(frac1.get_fraction())  # Output: "5"

frac2 = Fraction("5/7")
print(frac2.get_fraction())  # Output: "5/7"

frac3 = Fraction(-5, -7)
print(frac3.get_fraction())  # Output: "5/7"

frac4 = Fraction(123)
print(frac4.get_fraction())  # Output: "123"

frac5 = Fraction("    -5/7    ")
print(frac5.get_fraction())  # Output: "-5/7"

# gcd examples
print(Fraction.gcd(15, 5))  # Output: 5
print(Fraction.gcd(0, 0))   # Output: 0
print(Fraction.gcd(15, 0))  # Output: 15