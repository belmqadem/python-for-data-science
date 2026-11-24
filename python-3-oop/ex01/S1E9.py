from abc import ABC, abstractmethod


class Character(ABC):
    """An abstract base class for all characters."""

    def __init__(self, first_name: str, is_alive=True):
        """Constructor of Character class."""
        self.first_name = first_name
        self.is_alive = is_alive

    def toggleHealthState(self):
        """Method to change health state for a character."""
        self.is_alive = not self.is_alive

    @abstractmethod
    def die(self):
        """Abstract method to be implemented by subclasses."""
        pass


class Stark(Character):
    """A class representing a character from Stark family."""

    def die(self):
        """Method to set is_alive to false."""
        self.is_alive = False


if __name__ == "__main__":
    pass
