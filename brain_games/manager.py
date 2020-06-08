import prompt


GAMES_COUNT = 3


def welcome_user():
    print()
    print("Welcome to the Brain Games!")


def get_users_name():
    print()
    user = prompt.string("May I have your name? ")
    print("Hello, {}!".format(user))
    return user


def run_game(game):
    welcome_user()
    print(game.start_text)
    user = get_users_name()
    user_result = 0
    while user_result < GAMES_COUNT:
        question, ideal_answer = game.get_question_and_answer()

        print("Question: {}".format(question))
        answer = prompt.string("Your answer: ")
        if answer == ideal_answer:
            print("Correct!")
            user_result += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                answer, ideal_answer))
            print("Let's try again, {}!".format(user))
    print("Congratulations, {}!".format(user))
