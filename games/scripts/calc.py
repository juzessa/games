from games.games.calc import calc_game
from games.engine import engine


def calc():
    description = 'What is the result of the expression?'
    engine(description, calc_game)
    

if __name__ == "__main__":
    calc()