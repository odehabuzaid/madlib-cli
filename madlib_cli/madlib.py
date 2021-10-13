import getpass
import os
import re


def read_template(path: str):
    """
    - open the file and return a stripped string of the file’s contents

    Returns:
        String: stripped content of the file
    """
    try:
        with open(path) as file:
            return file.read().strip()

    except Exception as err:
        if err.__cause__ is FileNotFoundError:
            raise FileNotFoundError(err.__cause__)


def parse_template(content: str):
    """
     - takes template string and returns a string with language parts removed and a separate list of those language parts.

    Returns:
        String: stripped content of the file
    """
    pat = r"(?<=\{).+?(?=\})"
    language_parts = re.findall(pat, content)
    for part in language_parts:
        content = re.sub("{}".format(part), "", content)

    return content, tuple(language_parts)


def merge(*args):
    """
    - takes a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
    Returns:
        String: merged string
    """
    content, user_guesses = args
    for part in user_guesses:
        content = content.replace("{}".format("{}"), "{}".format(part), 1)

    content = " ".join(content.split())
    return content


def save_file(text: str):
    save_path = "./assets"
    file_name = "{}.txt".format(getpass.getuser())
    file_path = os.path.join(save_path, file_name)
    try:
        with open(file_path, "w") as file:
            file.write(text)
    except Exception as err:
        raise err.__cause__




