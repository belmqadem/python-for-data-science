def count_chars(string: str):
    """
    Docstring for count_chars
    :param string: The first argument
    :type string: str
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


def main(argv: str):
    """
    Docstring for main
    :param argv: The first argument
    :type argv: str
    """
    if len(argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(argv) == 2 and argv[1] != "":
        user_input = argv[1]
    else:
        while True:
            user_input = input()
            if user_input != "":
                break

    chars = count_chars(user_input)
    print(f"The text contains {chars[0]} characters:\n\
{chars[1]} upper letters\n\
{chars[2]} lower letters\n\
{chars[3]} punctuation marks\n\
{chars[4]} spaces\n\
{chars[5]} digits")


if __name__ == "__main__":
    from sys import argv
    try:
        main(argv)
    except AssertionError as e:
        print(f"AssertionError: {e}")
