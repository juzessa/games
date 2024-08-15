import random


def is_even(num: str) -> bool:
    return num % 2 == 0


def even_game():
    number = random.randint(0, 1000)
    question = f'Question: {number}'
    correct_answer = ['yes', 'no'][number % 2]
    return question, correct_answer
