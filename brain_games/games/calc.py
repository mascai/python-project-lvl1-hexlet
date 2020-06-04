from random import randint, choice


start_text = 'What is the result of the expression?'


def get_question_and_answer():
    lhs = randint(0, 1000)
    rhs = randint(0, 1000)
    mode = choice("-+*")
    if mode == '+':
        result = lhs + rhs
    elif mode == '-':
        result = lhs - rhs
    elif mode == '*':
        result = lhs * rhs
    question = "{} {} {}".format(lhs, mode, rhs)
    correct_answer = str(result)
    return question, correct_answer
