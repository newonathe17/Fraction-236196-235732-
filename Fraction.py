import math

class Fraction():
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):
            # Attempt to split the string into numerator and denominator
            try:
                numerator, denominator = numerator.strip().split('/')
                numerator = int(numerator)
                denominator = int(denominator)
            except ValueError:
                # If parsing fails, default to 0/1
                self.numerator = 0
                self.denominator = 1
                return

        elif not isinstance(numerator, int) or not isinstance(denominator, int):
            # Ensure both numerator and denominator are integers
            self.numerator = 0
            self.denominator = 1
            return

        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        if denominator < 0:
            # Move negative sign to the numerator
            numerator = -numerator
            denominator = -denominator

        # Simplify the fraction using GCD
        greatest_common_divisor = self.gcd(abs(numerator), abs(denominator))

        if greatest_common_divisor != 0:
            # Divide both numerator and denominator by GCD to simplify
            self.numerator = numerator // greatest_common_divisor
            self.denominator = denominator // greatest_common_divisor
        else:
            # If GCD is 0, retain original values (shouldn't happen for valid fractions)
            self.numerator = numerator
            self.denominator = denominator

    @staticmethod
    def gcd(a, b):
        if a == 0 or b == 0:
            return 0  # Return 0 if either number is 0 (GCD is undefined in this case)
        return math.gcd(a, b)  # Use built-in function for calculating GCD

    def get_numerator(self):
        return str(self.numerator)

    def get_denominator(self):
        return str(self.denominator)

    def get_fraction(self):
        if self.denominator == 1:
            return str(self.numerator)  # If denominator is 1, just return the numerator
        return f"{self.numerator}/{self.denominator}"
