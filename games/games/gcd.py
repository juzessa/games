import random

from math import gcd


def gcd_game():
    description = 'Find the greatest common divisor of given numbers.'
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    correct_answer = gcd(number1, number2)
    question = f'Question: {number1} {number2}'
    return description, question, str(correct_answer)
