class PercentageCalculator():
    @staticmethod
    def calculate(a, b):
        if b == 0:
            return 0
        return (100.0 * a) / b