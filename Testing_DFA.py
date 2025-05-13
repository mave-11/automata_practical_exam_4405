import DFA_div_3
import unittest


def precond_dfa(input_str):
    state = 'q0'  # Initial state
    for sym in input_str:
        match state:
            case 'q0':
                state = 'q1' if sym == '1' else 'q0'
            case 'q1':
                state = 'q2' if sym == '1' else 'q1'
            case 'q2':
                state = 'q3' if sym == '1' else 'q2'
            case 'q3':
                state = 'q1' if sym == '1' else 'q3'
    return state == 'q3'  # Only q3 is accepting now


class TestDFA(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(precond_dfa(''))

    def test_zero_ones_non_empty(self):
        self.assertFalse(precond_dfa('0'))
        self.assertFalse(precond_dfa('000'))
        self.assertFalse(precond_dfa('000000'))

    def test_three_ones(self):
        self.assertTrue(precond_dfa('111'))  # All consecutive
        self.assertTrue(precond_dfa('10101'))  # Spread out
        self.assertTrue(precond_dfa('1100010101'))  # With multiple zeros

    def test_six_ones(self):
        self.assertTrue(precond_dfa('111111'))  # Consecutive
        self.assertTrue(precond_dfa('101010101'))  # Spread pattern
        self.assertTrue(precond_dfa('111000111'))  # With zeros

    def test_non_divisible_counts(self):
        # 1 one
        self.assertFalse(precond_dfa('1'))
        self.assertFalse(precond_dfa('1000'))

        # 2 ones
        self.assertFalse(precond_dfa('11'))
        self.assertFalse(precond_dfa('01010'))

        # 4 ones
        self.assertFalse(precond_dfa('1111'))
        self.assertFalse(precond_dfa('10111'))

        # 5 ones
        self.assertFalse(precond_dfa('11111'))
        self.assertFalse(precond_dfa('110101'))

    def test_edge_cases(self):
        # Exactly 3 with leading/trailing zeros
        self.assertTrue(precond_dfa('01110'))
        self.assertTrue(precond_dfa('000111000'))

        # Mixed long string
        self.assertTrue(precond_dfa('101' * 1000))  # 3000 ones
        self.assertFalse(precond_dfa('101' * 1000 + '1'))  # 3001 ones


if __name__ == '__main__':
    unittest.main()