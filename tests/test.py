from unittest import TestCase
from .example_classes import Calculator, Displayer
from prophepy.exceptions import MethodWasNotCalledError, UndefinedMockBehaviorError
from prophepy import prophesize

class TestMocking(TestCase):
    def test_specify_behavior(self):
        calculator = prophesize(Calculator)
        displayer = Displayer(calculator._reveal())
        # We specify the behavior… We can make the calculator
        # do whatever we want!
        calculator.add(2, 5)._will_return(18)
        self.assertEqual(displayer.display_addition(2, 5), '2 + 5 = 18')

    def test_function_is_called(self):
        calculator = prophesize(Calculator)
        displayer = Displayer(calculator._reveal())

        calculator.add(2, 5)._will_return(18)
        calculator.add(2, 5)._should_be_called()
        self.assertEqual(displayer.display_addition(2, 5), '2 + 5 = 18')
        calculator.check_prophecies()

    def test_function_is_called_with_bad_arguments_exception(self):
        calculator = prophesize(Calculator)
        displayer = Displayer(calculator._reveal())

        calculator.add(2, 5)._will_return(18)

        # This method is never called with these arguments
        calculator.add(2, 8)._should_be_called()
        self.assertEqual(displayer.display_addition(2, 5), '2 + 5 = 18')

        with self.assertRaises(MethodWasNotCalledError):
            calculator.check_prophecies()

    def test_function_is_not_called_exception(self):
        calculator = prophesize(Calculator)
        displayer = Displayer(calculator._reveal())

        calculator.add(2, 5)._will_return(18)

        # This method is never called
        calculator.multiply(2, 8)._should_be_called()
        self.assertEqual(displayer.display_addition(2, 5), '2 + 5 = 18')

        with self.assertRaises(MethodWasNotCalledError):
            calculator.check_prophecies()

    def test_behavior_was_not_defined(self):
        calculator = prophesize(Calculator)
        displayer = Displayer(calculator._reveal())

        # The behavior was never defined (add(2, 8) method from Calculator)
        with self.assertRaises(UndefinedMockBehaviorError):
            displayer.display_addition(2, 5)
