import prompt
import random
from .hello import hello


def calc_game():
    name = hello()
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        number1 = random.randint(0, 100)
        number2 = random.randint(0, 100)
        operation = random.choice(['+', '-', '*'])
        correct_answer = {'+': number1 + number2, '-': number1 - number2, '*': number1 * number2}[operation]
        print(f'Question: {number1} {operation} {number2}')
        answer = int(prompt.string('Your answer: '))
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            return
        
        if i == 2:
            print(f'Congratulations, {name}!')
            return
        
if __name__ == "__main__":
    calc_game()
