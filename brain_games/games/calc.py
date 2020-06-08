from random import randint, choice
from operator import mul, add, sub


start_text = 'What is the result of the expression?'


def get_question_and_answer():
    lhs = randint(0, 1000)
    rhs = randint(0, 1000)
    mode = choice("-+*")
    if mode == '+':
        result = add(lhs, rhs)
    elif mode == '-':
        result = sub(lhs, rhs)
    elif mode == '*':
        result = mul(lhs, rhs)
    question = "{} {} {}".format(lhs, mode, rhs)
    correct_answer = str(result)
    return question, correct_answer
