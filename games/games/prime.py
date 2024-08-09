import random


def is_prime(num):
    pass


def prime_game():
    number = random.randint(0, 1000)
    question = f'Question: {number}'
    correct_answer = ['yes', 'no'][is_prime(number)]
    return question, correct_answer
