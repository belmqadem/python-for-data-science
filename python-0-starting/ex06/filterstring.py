from sys import argv
from ft_filter import ft_filter


def main(argv):
    """
    A program that takes a string and an integer as command-line arguments,
    filters the words in the string based on their length, and prints the
    filtered words.
    :param argv: List of command-line arguments. The first argument
    is the script name, the second argument is the string to be filtered,
    and the third argument is the length threshold.
    :type argv: list
    """
    if len(argv) != 3:
        raise AssertionError("the arguments are bad")
    try:
        length = int(argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    words = argv[1].split()
    filtered = ft_filter(lambda word: len(word) > length, words)
    print(list(filtered))


if __name__ == "__main__":
    try:
        main(argv)
    except AssertionError as e:
        print(f"AssertionError: {e}")
