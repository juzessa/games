import prompt
from games.utils import hello

LEVEL = 3


def engine(description, function):
    name = hello()
    print(description)
    counter = 0
    while counter < LEVEL:
        question, correct_answer = function()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\
                    \nLet's try again, {name}!")
            return
        print('Correct!')
        counter += 1

    print(f'Congratulations, {name}!')
    return


if __name__ == "__main__":
    engine()
