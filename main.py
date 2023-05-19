"""
Напишите, пожалуйста, программу на любом языке программирования, которая поместит + (2+3), - (3-2), или ничего ( ) в
промежутках между цифрами от 9 до 0 (в таком порядке) так, чтобы в результате получилось 200.
Например: 98+76-5+43-2-10=200.
"""

from random import choice

numbers: str = "9876543210"
expression: str = ""

possible_operators: tuple = ("+", "-", "")

while True:
    expression = ""
    for i, v in enumerate(numbers):
        expression += v
        if i != 9:
            expression += choice(possible_operators)
    if eval(expression) == 200:
        break

print(f"{expression}=200")
