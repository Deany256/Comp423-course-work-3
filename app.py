from random import choice
from email_validation import (
    creating_an_answer,
    extract_user,
    is_valid_email,
    random_string,
    spotting_word,
    select_random_number,
)


def random_disconnect():
    minimum = 1
    maximum = 10
    if select_random_number(minimum, maximum) == True:
        print("Disconnected ...")
        quit()


PROBLEM_LIST = [
    "library",
    "wifi",
    "deadline",
    "coffee",
    "absence",
    "kitchen",
]
OPERATOR_NAME = [
    "James",
    "Robert",
    "mary",
    "Jennifer",
]
ANSWERS = {
    "library": "the library is closed",
    "wifi": "the wifi coverage is excellent",
    "coffee": "the cafe is open at the moment",
    "deadline": "your deadline has been extended",
    "absence": "your absence will be noted",
    "kitchen": "the Poppleton Kitchen is open Mon-Fri 10:00-3:00",
}
RESPONSES = [
    "Hmmmm.",
    "Huh.",
    "You should try working on this system.",
    "Oh, my.",
    "That is interesting",
    "Oh, yes, I see",
    "Tell me more",
]
END_PROGRAM_KEYWORDS = [
    "exit",
    "quit",
    "bye",
    "goodbye",
    "seeya",
    "Exit",
    "Quit",
    "Bye",
    "Good bye",
    "Goodbye",
    "Seeya",
]

if __name__ == "__main__":
    print("Welcome to Pop Chat.")
    print("One of our operators will be pleased to help you today.")
    domain = "pop.ac.uk"
    email = input("Please enter your Poppleton email address: ").lower()
    random_disconnect()
    if is_valid_email(email, domain) == True:
        user_name = extract_user(email).title()
        print(f"Hello {user_name}! Thank you, and welcome to PopChat")
    else:
        print("please enter a valid email")
        quit()
    random_disconnect()
    print(
        f"My name is {random_string(OPERATOR_NAME)}, and it will be my pleasure to help you."
    )
    user_input = input("How can I help you: ").lower()
    random_disconnect()
    while True:
        if spotting_word(user_input, PROBLEM_LIST) == True:
            print(creating_an_answer(user_input, PROBLEM_LIST, ANSWERS))
            user_input = input("-->")
            random_disconnect()
        else:
            if spotting_word(user_input, END_PROGRAM_KEYWORDS) == True:
                print("bye")
                print()
                print(f"Thanks, {user_name}, for using PopChat. See you again soon.")
                quit()
            else:
                print(random_string(RESPONSES))
                user_input = input("-->")
