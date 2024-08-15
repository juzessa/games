from games.games.even import even_game
from games.engine import engine


def even():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine(description, even_game)
    

if __name__ == "__main__":
    even()