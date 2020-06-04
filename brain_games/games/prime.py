from random import randint


start_text = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num > 1:
        for i in range(2, (num // 2) + 1):
            if (num % i) == 0:
                return False
        return True


def get_question_and_answer():
    number = randint(1, 1000)
    question = str(number)
    answer = "yes"
    if not is_prime(number):
        answer = "no"
    return question, answer
