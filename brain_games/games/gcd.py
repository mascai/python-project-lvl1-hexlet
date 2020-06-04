from random import randint


start_text = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def get_question_and_answer():
    lhs = randint(0, 1000)
    rhs = randint(0, 1000)
    question = "{} {}".format(lhs, rhs)
    return question, str(gcd(lhs, rhs))
