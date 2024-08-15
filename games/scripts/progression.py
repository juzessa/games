from games.games.progression import progression_game
from games.engine import engine


def progression():
    description = 'What number is missing in the progression?'
    engine(description, progression_game)
    

if __name__ == "__main__":
    progression()