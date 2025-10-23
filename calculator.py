# app/calculator.py
from typing import Union


def safe_divide(numerator: Union[int, float], denominator: Union[int, float]) -> Union[float, str]:
    """
    Делит два числа. Использует Type Hinting для надежности.
    Возвращает ошибку, если знаменатель равен нулю.
    """
    if denominator == 0:
        return "Error: Division by zero is not allowed."
    return float(numerator / denominator)


def power_of_two(number: int) -> int:
    """Возвращает число в степени 2."""
    return number ** 2
