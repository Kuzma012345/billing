import string
import random


def random_string():
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(20))
    return rand_string


def random_decimal():
    random_dec = round(10000 * random.random(), 4)
    return random_dec


def random_percent():
    random_perc = round(100 * random.random(), 4)
    return random_perc


def random_int():
    return random.randint(10, 1000)
