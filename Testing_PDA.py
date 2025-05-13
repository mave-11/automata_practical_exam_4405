
from checker_PDA import is_balanced
import unittest

class TestIsBalanced(unittest.TestCase):
    def test_is_balanced(self):
        test_cases = [
            # Valid balanced cases
            ("", True),          # Empty string
            ("()", True),         # Simple balanced
            ("(()())", True),     # Nested balanced
            ("((()))", True),     # Fully nested
            ("()()()", True),     # Sequential balanced
            
            # Unbalanced cases
            ("(", False),         # Single open
            (")", False),         # Single close
            ("())(", False),     # Mismatched order
            ("())", False),       # Extra close
            ("(()", False),      # Extra open
            (")(", False),        # Close before open
            ("(()))", False),     # More closes than opens
            
            # Invalid characters
            ("(a)", False),       # Invalid char inside
            ("a", False),        # Single invalid char
            ("())x", False),     # Invalid char after valid sequence
            ("x()", False),      # Invalid char at start
            ("()x", False),      # Invalid char at end
        ]
        
        for input_str, expected in test_cases:
            with self.subTest(input=input_str, expected=expected):
                self.assertEqual(is_balanced(input_str), expected)

if __name__ == "__main__":
    unittest.main()



    