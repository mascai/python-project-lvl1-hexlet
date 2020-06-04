from random import randint


start_text = 'Answer "yes" if number even otherwise answer "no".'


def is_even(n):
    return n % 2 == 0


def get_question_and_answer():
    n = randint(0, 1000)
    question = str(n)
    answer = "yes"
    if not is_even(n):
        answer = "no"
    return question, answer
