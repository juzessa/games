from games.games.prime import prime_game
from games.engine import engine


def prime():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine(description, prime_game)
    

if __name__ == "__main__":
    prime()