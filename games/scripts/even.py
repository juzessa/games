import prompt
import random


def even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = random.randint(0, 1000)
        print(f'Question: {number}')
        correct_answer = ['yes', 'no'][number % 2]
        answer = prompt.string('Your answer: ')
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
    even_game()

