import subprocess
import sys
import unittest


class TestHello(unittest.TestCase):
    """Comprehensive unit tests for hello.py."""

    def run_hello(self, *args):
        """Helper to run hello.py with the given arguments and return CompletedProcess."""
        return subprocess.run(
            [sys.executable, "hello.py", *args],
            capture_output=True,
            text=True,
        )

    # --- Happy path ---

    def test_greeting_with_simple_name(self):
        result = self.run_hello("World")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hello, World!")

    def test_greeting_with_first_name(self):
        result = self.run_hello("Alice")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hello, Alice!")

    def test_greeting_uses_only_first_argument(self):
        """When multiple arguments are provided, only the first is used."""
        result = self.run_hello("Bob", "extra")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hello, Bob!")

    def test_greeting_with_numeric_name(self):
        result = self.run_hello("42")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hello, 42!")

    def test_greeting_with_name_containing_spaces(self):
        result = self.run_hello("John Doe")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hello, John Doe!")

    def test_greeting_with_special_characters(self):
        result = self.run_hello("O'Brien")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hello, O'Brien!")

    def test_greeting_with_unicode_name(self):
        result = self.run_hello("Ångström")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hello, Ångström!")

    def test_greeting_with_hyphenated_name(self):
        result = self.run_hello("Mary-Jane")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hello, Mary-Jane!")

    def test_greeting_output_format(self):
        """Output must start with 'Hello, ' and end with '!'."""
        result = self.run_hello("Test")
        self.assertTrue(result.stdout.strip().startswith("Hello, "))
        self.assertTrue(result.stdout.strip().endswith("!"))

    # --- Error path ---

    def test_no_argument_exits_with_code_1(self):
        result = self.run_hello()
        self.assertEqual(result.returncode, 1)

    def test_no_argument_prints_error_message(self):
        result = self.run_hello()
        self.assertIn("Error", result.stdout)
        self.assertIn("name", result.stdout.lower())

    def test_no_argument_prints_usage(self):
        result = self.run_hello()
        self.assertIn("Usage", result.stdout)
        self.assertIn("hello.py", result.stdout)

    def test_no_argument_produces_no_greeting(self):
        result = self.run_hello()
        self.assertNotIn("Hello,", result.stdout)

    # --- Output stream checks ---

    def test_successful_greeting_has_no_stderr(self):
        result = self.run_hello("World")
        self.assertEqual(result.stderr, "")

    def test_error_output_goes_to_stdout(self):
        """The script prints its error to stdout (not stderr)."""
        result = self.run_hello()
        self.assertNotEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
