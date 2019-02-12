# Prophepy

Mocks made easy in your python tests. Greatly inspired by PHP's [Prophecy](https://github.com/phpspec/prophecy).

## Usage

```python
from examples.calculator import Calculator
from examples.displayer import Displayer
from src.prophepy import prophesize

    calculator = prophesize(Calculator)
    displayer = Displayer(calculator._reveal())

    calculator.add(2, 3)._should_be_called()
    calculator.add(2, 3)._will_return(5)
    displayer.display_add(2, 3)

    calculator.check_prophecies()
```
