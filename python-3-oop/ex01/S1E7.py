from S1E9 import Character


class Baratheon(Character):
    """A class representing a character from Baratheon family."""

    def __init__(
        self,
        first_name: str,
        is_alive=True,
        family_name="Baratheon",
        eyes="brown",
        hairs="dark",
    ):
        """Constructor of Baratheon class."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        """String representation of Baratheon character."""
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self) -> str:
        """Official string representation of Baratheon character."""
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def die(self):
        """Method to set is_alive to false."""
        self.is_alive = False


class Lannister(Character):
    """A class representing a character from Lannister family"""

    def __init__(
        self,
        first_name: str,
        is_alive=True,
        family_name="Lannister",
        eyes="blue",
        hairs="light",
    ):
        """Constructor of Lannister class."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        """String representation of Lannister character."""
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self) -> str:
        """Official string representation of Lannister character."""
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool):
        """Static method to create a Lannister character."""
        return Lannister(first_name, is_alive)

    def die(self):
        """Method to set is_alive to false."""
        self.is_alive = False


if __name__ == "__main__":
    pass
