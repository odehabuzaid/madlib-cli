
from madlib import merge, parse_template, read_template, save_file

"""
    TODO [x] : create a function that takes path and returns a stripped string of the file’s contents.
    TODO [x] : create a function that takes template string and returns a string with language parts removed and a separate list of those language parts.    
    TODO [x] : create a function that takes a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
"""
"""
? Stretch Goals
? [x] 1- Figure out / research a way to verify terminal input/output.
? [x]2- Test that completed madlib is properly written to disk with correct content.
"""

import getpass

from pyfiglet import Figlet
from termcolor import colored


def welcome():
    """
    Print a welcome message to the user,
        - explaining the  process
        - command line interactions
    """
    logo = Figlet(font="standard")
    print(colored(logo.renderText("madLib"), "red"))
    print(colored(logo.renderText("Hello ,{}\n".format(getpass.getuser())), "cyan"))
    print(colored(("=" * 80), "red"))
    print(colored(("Welcome to madLib!"), "white"))
    print(
        colored(
            ("This program will help you create a madlib from a template."), "white"
        )
    )
    print(colored(("You will be prompted for words to fill in the blanks.\n"), "white"))
    print(colored(("Type (exit) to end this program"), "cyan"))
    input(colored(("Press (enter) to continue..."), "cyan"))
    print(colored(("{} \n".format("=" * 80)), "red"))


def main():
    """
    - [x] Read a template Madlib file. and parse that file into usable parts.
    - [x] Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
    - [x] With the collected user inputs, populate the template such that each provided input is placed into the    correct position within the template.
    """
    
    path = "./assets/content.txt"
    file_content = read_template(path)
    print(file_content)
    content, language_parts = parse_template(file_content)
    print(type(language_parts))
    print(type(content))
    print(colored(content, "green"))
    print(
        colored(
            ("\n Enter the words to fill in between above curly brackets:\n"), "cyan"
        )
    )
    user_guesses = []
    idx = 0
    while len(user_guesses) != len(language_parts):
        guess = input(colored(("{} : ".format(language_parts[idx])), "cyan"))
        if len(guess) > 0:
            if guess.lower() == "exit":
                print(colored(("you entries are not completed ..."), "red"))
                break
            user_guesses.append(guess)
            idx += 1

    print(colored(("\n Your Madlib :\n"), "cyan"))
    merged_text = merge(content, user_guesses)
    print("{} \n".format(merged_text))
    save_file(merged_text)


if __name__ == '__main__':
    welcome()
    main()
