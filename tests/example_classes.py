class Calculator:
    def __init__(self, name, **kwargs):
        self.name = name
        self.values = kwargs

    def multiply(self, *args):
        product = 1
        for arg in args:
            product = product * arg

        return product

    def add(self, *args):
        return sum(args)

class Displayer:
    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def display_addition(self, *args) -> str:
        '''
        If called with (3, 5) will return '3 + 5 = {sum given by the
        calculator}'
        '''
        total = str(self.calculator.add(*args))
        args = [str(arg) for arg in args]

        return f"{' + '.join(args)} = {total}"
