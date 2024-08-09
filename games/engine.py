import prompt
from games.utils import hello
from games.games.even import even_game
from games.games.calc import calc_game
from games.games.gcd import gcd_game
from games.games.progression import progression_game
from games.games.prime import prime_game

LEVEL = 3
DESCRIPTION1 = 'Answer "yes" if the number is even, otherwise answer "no".'
DESCRIPTION2 = 'What is the result of the expression?'
DESCRIPTION3 = 'Find the greatest common divisor of given numbers.'
DESCRIPTION4 = 'What number is missing in the progression?'
DESCRIPTION5 = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def engine(game_name):
    name = hello()
    description = {
        'even': DESCRIPTION1,
        'calc': DESCRIPTION2,
        'gcd': DESCRIPTION3,
        'progression': DESCRIPTION4,
        'prime': DESCRIPTION5}[game_name]
    print(description)
    for i in range(LEVEL):
        question, correct_answer = {'even': even_game, 'calc': calc_game, 'gcd': gcd_game,
                                    'progression': progression_game, 'prime': prime_game}[game_name]()
        print(question)
        if game_name in ['even', 'prime']:
            answer = prompt.string('Your answer: ')
        else:
            answer = int(prompt.string('Your answer: '))
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
    arg = prompt.string('Choose game: even/calc/gcd/progression/prime/ ')
    if arg in ['even', 'calc', 'gcd', 'progression', 'prime']:
        engine(arg)
    else:
        print('Wrong name, try again')
