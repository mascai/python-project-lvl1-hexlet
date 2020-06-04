from random import randint


start_text = "What number is missing in the progression?"
LEN = 10


def get_question_and_answer():
    progression = []
    start_num = randint(1, 10)
    step = randint(1, 10)
    last = LEN * step + start_num
    for i in range(start_num, last, step):
        progression.append(i)

    temp = randint(0, LEN - 1)
    answer = str(progression[temp])
    progression[temp] = '..'
    question = " ".join(str(item) for item in progression)
    return question, answer
