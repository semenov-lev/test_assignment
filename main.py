"""
Напишите, пожалуйста, программу на любом языке программирования, которая поместит + (2+3), - (3-2), или ничего ( ) в
промежутках между цифрами от 9 до 0 (в таком порядке) так, чтобы в результате получилось 200.
Например: 98+76-5+43-2-10=200.
"""

from itertools import product, zip_longest

NUMBERS: tuple = ("9", "8", "7", "6", "5", "4", "3", "2", "1", "0")

possible_combinations = product(("+", "-", ""), repeat=9)

for combination in possible_combinations:
    expression_raw: list = list(zip_longest(NUMBERS, combination, fillvalue=''))
    expression: str = "".join(map("".join, expression_raw))

    if eval(expression) == 200:
        print(f"{expression}=200")
