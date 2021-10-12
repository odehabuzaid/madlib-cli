"""
Print a welcome message to the user, 
- explaining the Madlib process 
- command line interactions

Read a template Madlib file. and parse that file into usable parts.

Prompt the user to submit a series of words to fit each of the required components of the Madlib template.

With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.

Make Me A Video Game!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!
! I the majestic and purple Scott have colored JB's laughing sister and plan to steal her tickled arrows!

What are a {Large Animal} and backpacking {Small Animal} to do? 
! What are a gorilla and backpacking butterfly to do?
Before you can help {A Girl's Name}, 
! Before you can help Betty,
you'll have to collect the {Adjective} {Plural Noun} 
! you'll have to collect the silly tests
and {Adjective} {Plural Noun} that open up the {Number 1-50} 
! and striped jackets that open up the 44 
worlds connected to A {First Name's} Lair. 
! worlds connected to Wilson's' Lair.
There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, 
! There are 3 leaves and 4 swords in the game,
along with hundreds of other goodies for you to find.

After the resulting Madlib has been completed, provide the completed response back to the user in the command line.

Write the completed text (!in red above)to a new file on your file system (in the repo).

Note: A smaller example file is included as well which can be handy when developing/testing.
! It was a {Adjective} and {Adjective} {Noun}.

*. Create and test a read_template function that takes in 
*. a path to text file 
*. returns a stripped string of the file’s contents.
!. read_template should raise a FileNotFoundError if path is invalid.

*. Create and test a parse_template function that takes in
*. template string 
*. returns a string with language parts removed and a separate list of those language parts.

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
"""


def read_template(path: str):
    try:
        with open(path) as file:
            return file.read().strip()
    except Exception as err:
        if err.__cause__ is FileNotFoundError:
            raise FileNotFoundError(err.__cause__)

import re


def parse_template(content: str):
    pat = r"(?<=\{).+?(?=\})"
    language_parts = re.findall(pat, content)
    for part in language_parts:
        content = re.sub('{}'.format(part), "", content)

    return content, language_parts


def merge():
    print()


path = "./Madlib .txt"
file_content = read_template(path)



content, language_parts = parse_template(file_content)

