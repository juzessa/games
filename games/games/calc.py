import random


def calc_game():
    description = 'What is the result of the expression?'
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    operation = random.choice(['+', '-', '*'])
    correct_answer = {
        '+': number1 + number2,
        '-': number1 - number2,
        '*': number1 * number2}[operation]
    question = f'Question: {number1} {operation} {number2}'
    return description, question, str(correct_answer)
