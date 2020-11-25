from string import ascii_letters
import random


def create_short():
    return ''.join(random.choices(ascii_letters, k=6))
