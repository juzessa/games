import random


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_game():
    number = random.randint(0, 1000)
    question = f'Question: {number}'
    correct_answer = ['no', 'yes'][is_prime(number)]
    return question, correct_answer
