def slugify(text) -> str:
    """
    Convert a string to a slug format by replacing spaces with hyphens and
    converting to lowercase.
    :param text: The input string to be converted.
    :type text: str
    :return: The slugified version of the input string.
    :rtype: str
    """
    return "-".join(text.split()).lower()


if __name__ == "__main__":
    pass
