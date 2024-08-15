import prompt
from games.utils import hello

LEVEL = 3


def engine(function):
    name = hello()
    description, _, _= function()
    print(description)
    for i in range(LEVEL):
        _, question, correct_answer = function()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            return

        if i == 2:
            print(f'Congratulations, {name}!')
            return


if __name__ == "__main__":
    engine()
