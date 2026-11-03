from sys import argv
from ft_filter import ft_filter


def main(argv):
    """
    A program that output a list of words from S that have a length
    greater than N
    :param argv: argument passed by the user
    :first argv: a string (S)
    :second argv: an integer (N)
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
