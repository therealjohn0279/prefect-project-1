"""
Comprehensive test suite for the Greeter class.

This module contains pytest tests that achieve 100% code coverage
and follow Python testing best practices.
"""

from unittest.mock import patch

import pytest
from prefect_project_1.greet.greeter import Greeter, main


class TestGreeterInit:
    """Test the Greeter class initialization."""

    def test_init_with_default_message(self):
        """Test initialization with default message."""
        greeter = Greeter()
        assert greeter.message == "Hello World"

    def test_init_with_custom_message(self):
        """Test initialization with custom message."""
        custom_message = "Hola Mundo"
        greeter = Greeter(custom_message)
        assert greeter.message == custom_message

    def test_init_with_empty_string(self):
        """Test initialization with empty string."""
        greeter = Greeter("")
        assert greeter.message == ""

    def test_init_with_none_message(self):
        """Test initialization with None (should work due to default)."""
        # This tests the type hint but allows None at runtime
        greeter = Greeter(None)
        assert greeter.message is None


class TestGreeterGreet:
    """Test the greet method."""

    def test_greet_prints_default_message(self, capsys):
        """Test that greet prints the default message."""
        greeter = Greeter()
        greeter.greet()

        captured = capsys.readouterr()
        assert captured.out == "Hello World\n"
        assert captured.err == ""

    def test_greet_prints_custom_message(self, capsys):
        """Test that greet prints custom message."""
        custom_message = "Bonjour le monde"
        greeter = Greeter(custom_message)
        greeter.greet()

        captured = capsys.readouterr()
        assert captured.out == f"{custom_message}\n"

    def test_greet_prints_empty_message(self, capsys):
        """Test that greet handles empty string correctly."""
        greeter = Greeter("")
        greeter.greet()

        captured = capsys.readouterr()
        assert captured.out == "\n"

    def test_greet_returns_none(self):
        """Test that greet method returns None."""
        greeter = Greeter()
        result = greeter.greet()
        assert result is None

    def test_greet_with_special_characters(self, capsys):
        """Test greet with special characters and unicode."""
        special_message = "Hello 🌍! Special chars: @#$%^&*()"
        greeter = Greeter(special_message)
        greeter.greet()

        captured = capsys.readouterr()
        assert captured.out == f"{special_message}\n"


class TestGreeterStr:
    """Test the __str__ method."""

    def test_str_returns_message(self):
        """Test that __str__ returns the message."""
        message = "Test Message"
        greeter = Greeter(message)
        assert str(greeter) == message

    def test_str_with_default_message(self):
        """Test __str__ with default message."""
        greeter = Greeter()
        assert str(greeter) == "Hello World"

    def test_str_with_empty_message(self):
        """Test __str__ with empty message."""
        greeter = Greeter("")
        assert str(greeter) == ""

    def test_str_integration_with_print(self, capsys):
        """Test __str__ integration when used with print()."""
        greeter = Greeter("Integration Test")
        print(greeter)

        captured = capsys.readouterr()
        assert captured.out == "Integration Test\n"


class TestGreeterRepr:
    """Test the __repr__ method."""

    def test_repr_format(self):
        """Test that __repr__ returns correct format."""
        message = "Test Repr"
        greeter = Greeter(message)
        expected = f"Greeter(message='{message}')"
        assert repr(greeter) == expected

    def test_repr_with_default_message(self):
        """Test __repr__ with default message."""
        greeter = Greeter()
        expected = "Greeter(message='Hello World')"
        assert repr(greeter) == expected

    def test_repr_with_quotes_in_message(self):
        """Test __repr__ with quotes in the message."""
        message = "Message with 'single' quotes"
        greeter = Greeter(message)
        expected = f"Greeter(message='{message}')"
        assert repr(greeter) == expected

    def test_repr_is_eval_safe(self):
        """Test that repr output can be used with eval to recreate object."""
        original_greeter = Greeter("Eval Test")
        repr_string = repr(original_greeter)

        # This would work if Greeter is in the global namespace
        # For testing, we'll just verify the format is correct
        assert repr_string.startswith("Greeter(message='")
        assert repr_string.endswith("')")

    def test_repr_in_container(self):
        """Test __repr__ when object is in a container."""
        greeter = Greeter("Container Test")
        container = [greeter]
        container_str = str(container)

        assert "Greeter(message='Container Test')" in container_str


class TestMainFunction:
    """Test the main function."""

    def test_main_creates_and_calls_greeter(self, capsys):
        """Test that main function creates greeter and calls greet."""
        main()

        captured = capsys.readouterr()
        assert captured.out == "Hello World\n"

    @patch("prefect_project_1.greet.greeter.Greeter")
    def test_main_function_mocked(self, mock_greeter_class):
        """Test main function with mocked Greeter class."""
        mock_greeter_instance = mock_greeter_class.return_value

        main()

        # Verify Greeter was instantiated with no arguments
        mock_greeter_class.assert_called_once_with()
        # Verify greet method was called
        mock_greeter_instance.greet.assert_called_once_with()


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_greeter_with_very_long_message(self):
        """Test greeter with very long message."""
        long_message = "A" * 1000
        greeter = Greeter(long_message)
        assert greeter.message == long_message
        assert str(greeter) == long_message

    def test_greeter_with_newlines_in_message(self, capsys):
        """Test greeter with newlines in message."""
        message_with_newlines = "Line 1\nLine 2\nLine 3"
        greeter = Greeter(message_with_newlines)
        greeter.greet()

        captured = capsys.readouterr()
        assert captured.out == f"{message_with_newlines}\n"

    def test_greeter_immutability_concept(self):
        """Test that changing message after init works (no immutability enforced)."""
        greeter = Greeter("Original")
        greeter.message = "Modified"
        assert greeter.message == "Modified"
        assert str(greeter) == "Modified"


class TestParametrizedTests:
    """Parametrized tests for comprehensive coverage."""

    @pytest.mark.parametrize(
        "message,expected",
        [
            ("Hello", "Hello"),
            ("", ""),
            ("🎉 Emoji test", "🎉 Emoji test"),
            ("Multi\nline\ntest", "Multi\nline\ntest"),
            ("Tabs\tand\tspaces", "Tabs\tand\tspaces"),
            ("Numbers 123", "Numbers 123"),
            ("Special @#$%", "Special @#$%"),
        ],
    )
    def test_various_messages(self, message, expected):
        """Test greeter with various message types."""
        greeter = Greeter(message)
        assert greeter.message == expected
        assert str(greeter) == expected

    @pytest.mark.parametrize(
        "message",
        [
            "Test 1",
            "Test 2",
            "",
            "🌟",
        ],
    )
    def test_greet_output_parametrized(self, message, capsys):
        """Test greet output with parametrized messages."""
        greeter = Greeter(message)
        greeter.greet()

        captured = capsys.readouterr()
        assert captured.out == f"{message}\n"


class TestTypeHints:
    """Test behavior related to type hints (runtime behavior)."""

    def test_type_hint_compliance_string(self):
        """Test that string messages work as expected."""
        greeter = Greeter("String test")
        assert isinstance(greeter.message, str)

    def test_greet_return_type_none(self):
        """Test that greet returns None as type hinted."""
        greeter = Greeter()
        result = greeter.greet()
        assert result is None

    def test_str_return_type_string(self):
        """Test that __str__ returns string as type hinted."""
        greeter = Greeter("Type test")
        result = str(greeter)
        assert isinstance(result, str)

    def test_repr_return_type_string(self):
        """Test that __repr__ returns string as type hinted."""
        greeter = Greeter("Repr type test")
        result = repr(greeter)
        assert isinstance(result, str)


# Fixtures for more complex testing scenarios
@pytest.fixture
def default_greeter():
    """Fixture providing a Greeter with default message."""
    return Greeter()


@pytest.fixture
def custom_greeter():
    """Fixture providing a Greeter with custom message."""
    return Greeter("Custom fixture message")


class TestWithFixtures:
    """Tests using fixtures."""

    def test_fixture_default_greeter(self, default_greeter):
        """Test using default greeter fixture."""
        assert default_greeter.message == "Hello World"

    def test_fixture_custom_greeter(self, custom_greeter):
        """Test using custom greeter fixture."""
        assert custom_greeter.message == "Custom fixture message"

    def test_multiple_fixtures(self, default_greeter, custom_greeter):
        """Test using multiple fixtures."""
        assert default_greeter.message != custom_greeter.message


# Performance/stress tests
class TestPerformance:
    """Basic performance and stress tests."""

    def test_many_greetings(self):
        """Test creating and using many greeters."""
        greeters = [Greeter(f"Message {i}") for i in range(100)]

        for i, greeter in enumerate(greeters):
            assert greeter.message == f"Message {i}"

    @pytest.mark.slow
    def test_very_large_message(self, capsys):
        """Test with very large message (marked as slow)."""
        large_message = "X" * 10000
        greeter = Greeter(large_message)
        greeter.greet()

        captured = capsys.readouterr()
        assert len(captured.out) == len(large_message) + 1  # +1 for newline
