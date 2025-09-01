class Greeter:
    """A simple greeter class following Python conventions."""

    def __init__(self, message: str = "Hello World"):
        self.message = message

    def greet(self) -> None:
        """Print the greeting message."""
        print(self.message)

    def __str__(self) -> str:
        """String representation of the greeter."""
        return self.message

    def __repr__(self) -> str:
        """Developer representation of the greeter."""
        return f"Greeter(message='{self.message}')"


def main() -> None:
    """Main function to demonstrate the Greeter class."""
    greeter = Greeter()
    greeter.greet()
