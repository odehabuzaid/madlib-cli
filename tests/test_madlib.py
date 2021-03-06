import pytest
from madlib_cli.madlib import merge, parse_template, read_template, save_file


def test_read_template_returns_stripped_string():
    actual = read_template("./assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected

# @pytest.mark.skip("pending")
def test_save_template_raises_exception_with_bad_path():
        with open('./assets/test1.txt', "w"):
            save_file('It was a {Adjective} and {Adjective} {Noun}.')


@pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():
    with pytest.raises(FileNotFoundError):
        path = "assets\content.txt"
        read_template(path)


     

