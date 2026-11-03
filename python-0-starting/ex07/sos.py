from sys import argv


NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


def main(argv):
    """
    Program that takes a string as an argument and encodes it into Morse Code.
    :param argv: List of command-line arguments. The first argument
    is the script name, and the second argument is the string to be encoded.
    :type argv: list
    """
    if len(argv) != 2:
        raise AssertionError("the arguments are bad")
    try:
        morse_code = [NESTED_MORSE[c] for c in argv[1].upper()]
    except KeyError:
        raise AssertionError("the arguments are bad")
    print(" ".join(morse_code))


if __name__ == "__main__":
    try:
        main(argv)
    except AssertionError as e:
        print(f"AssertionError: {e}")
