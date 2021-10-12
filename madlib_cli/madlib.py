import getpass
import re

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
    print(colored(("You will be prompted for words to fill in the blanks."), "white"))
    input(colored(("Press enter to continue..."), "cyan"))
    print(colored(("=" * 80), "red"))


def main():
    """
    - [x] Read a template Madlib file. and parse that file into usable parts.
    - [x] Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
    - [x] With the collected user inputs, populate the template such that each provided input is placed into the    correct position within the template.
    """
    path = "./Madlib .txt"
    file_content = read_template(path)
    language_parts, content = parse_template(file_content)
    print(type(language_parts))
    print(type(content))
    print(colored(content, "green"))
    print(colored(("\n Enter the words to fill in the blanks :\n"), "cyan"))
    user_guesses = []
    for part in language_parts:
        guess = input(colored(("{} : ".format(part)), "cyan"))
        user_guesses.append(guess)

    merge(content, user_guesses)


"""
After the resulting Madlib has been completed, provide the completed response back to the user in the command line.

Write the completed text (!in red above)to a new file on your file system (in the repo).

Note: A smaller example file is included as well which can be handy when developing/testing.
! It was a {Adjective} and {Adjective} {Noun}.

*. Create and test a merge function that takes in 
*. a “bare” template and a list of user entered language parts,
*. and returns a string with the language parts inserted into the template.
 
? Stretch Goals
? 1- Figure out / research a way to verify terminal input/output.
? 2- Test that completed madlib is properly written to disk with correct content.
"""


"""
    TODO [x] : create a function that takes path and returns a stripped string of the file’s contents.
    TODO [x] : create a function that takes template string and returns a string with language parts removed and a separate list of those language parts.    
    TODO [x] : create a function that takes a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
"""


def read_template(path: str):
    try:
        with open(path) as file:
            return file.read().strip()
    except Exception as err:
        if err.__cause__ is FileNotFoundError:
            raise FileNotFoundError(err.__cause__)


def parse_template(content: str):
    pat = r"(?<=\{).+?(?=\})"
    language_parts = re.findall(pat, content)
    for part in language_parts:
        content = re.sub("{}".format(part), "", content)

    return tuple(language_parts), content


def merge(*args):
    content, user_guesses = args
    for part in user_guesses:
        content = content.replace("{}".format("{}"), "{} ".format(part), 1)
    
    content = content.strip()
    return content


if __name__ == "__main__":
    welcome()
    main()


# content, language_parts = parse_template(file_content)

# print(parse_template("It was a {Adjective} and {Adjective} {Noun}."))
