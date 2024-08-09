import random


def make_progression():
    start = random.randint(0, 50)
    step = random.randint(1, 10)
    length = random.randint(5, 20)
    progression = [i for i in range(start, start + step * length, step)]
    return progression


def progression_game():
    progression = make_progression()
    hide = random.randint(1, len(progression))
    correct_answer = progression[hide]
    progression[hide] = '..'
    question = f'Question: {' '.join(str(i) for i in progression)}'
    return question, correct_answer
