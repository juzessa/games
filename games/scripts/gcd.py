from games.games.gcd import gcd_game
from games.engine import engine


def gcd():
    description = 'Find the greatest common divisor of given numbers.'
    engine(description, gcd_game)
    

if __name__ == "__main__":
    gcd()