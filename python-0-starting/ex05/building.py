from sys import argv, stdin


def count_chars(string: str) -> tuple:
    """
    Count the number of upper-case characters, lower-case characters,
    punctuation characters, digits, and spaces in the given string.
    :param string: The string to analyze.
    :type string: str
    :return: A tuple containing the counts of each character type.
    :rtype: tuple
    """
    total = uppers = lowers = punctuations = digits = spaces = 0
    for c in string:
        if c.isupper():
            uppers += 1
        elif c.islower():
            lowers += 1
        elif c.isdigit():
            digits += 1
        elif c.isspace():
            spaces += 1
        else:
            punctuations += 1
        total += 1
    return (total, uppers, lowers, punctuations, spaces, digits)


def main(argv: list) -> None:
    """
    Count how much upper-case characters, lower-case characters,
    punctuation characters, digits, and spaces in the string passed
    as an argument.
    :param argv: List of command-line arguments. The first argument is the
    script name, and the second argument is the string to be analyzed.
    :type argv: list
    """
    if len(argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(argv) == 2 and argv[1] != "":
        user_input = argv[1]
    else:
        print("What is the text to count?")
        user_input = stdin.readline()

    chars = count_chars(user_input)
    print(f"The text contains {chars[0]} characters:\n\
{chars[1]} upper letters\n\
{chars[2]} lower letters\n\
{chars[3]} punctuation marks\n\
{chars[4]} spaces\n\
{chars[5]} digits")


if __name__ == "__main__":
    try:
        main(argv)
    except AssertionError as e:
        print(f"AssertionError: {e}")
