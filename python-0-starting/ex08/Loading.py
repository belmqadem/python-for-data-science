
import sys
from os import get_terminal_size
from time import time


def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progress bar every time a value is requested.

    :param lst: Iterable to decorate with a progress bar.
    :type lst: range
    """
    total = len(lst)
    count = 0

    terminal_width = get_terminal_size().columns
    bar_width = terminal_width - 30

    start = time()

    for item in lst:
        count += 1

        filled = int(count / total * bar_width)
        bar = "█" * filled + " " * (bar_width - filled)

        percent = int(count / total * 100)
        elapsed = time() - start

        sys.stdout.write(
            f"\r{percent}%|{bar}| {count}/{total} "
            f"[{elapsed:.2f}s]"
        )
        sys.stdout.flush()

        yield item

    if total == 0:
        return

    print()


if __name__ == "__main__":
    for elem in ft_tqdm(range(10)):
        pass
