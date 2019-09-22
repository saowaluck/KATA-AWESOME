import unittest
import random
import math
from unittest.mock import patch
from contextlib import ExitStack

class TestCaculation(unittest.TestCase):
    def test_random_left_operand_should_return_one_to_ten(self):
        actual = random_left_operand()

        expected = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'nine', 'ten']
        self.assertTrue(actual in expected)


    def test_random_right_operand_should_return_1_to_10(self):
        actual = random_right_operand()

        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(actual in expected)

    def test_random_operator_should_return_plus_minus_mul_div(self):
        actual = random_operator()

        expected = ['+', '-', '*', '/']
        self.assertTrue(actual in expected)


    def test_one_plus_1_should_return_2(self):
        with ExitStack() as stack:
            stack.enter_context(patch('__main__.random_left_operand', return_value='one'))
            stack.enter_context(patch('__main__.random_operator', return_value='+'))
            stack.enter_context(patch('__main__.random_right_operand', return_value=1))

            actual = calculation()

        expected = 2
        self.assertEqual(actual, expected)

    def test_three_minus_3_should_return_0(self):
        with ExitStack() as stack:
            stack.enter_context(patch('__main__.random_left_operand', return_value='three'))
            stack.enter_context(patch('__main__.random_operator', return_value='-'))
            stack.enter_context(patch('__main__.random_right_operand', return_value=3))

            actual = calculation()

        expected = 0
        self.assertEqual(actual, expected)

    def test_nine_mul_2_should_return_18(self):
        with ExitStack() as stack:
            stack.enter_context(patch('__main__.random_left_operand', return_value='nine'))
            stack.enter_context(patch('__main__.random_operator', return_value='*'))
            stack.enter_context(patch('__main__.random_right_operand', return_value=2))

            actual = calculation()

        expected = 18
        self.assertEqual(actual, expected)

    def test_ten_div_5_should_return_2(self):
        with ExitStack() as stack:
            stack.enter_context(patch('__main__.random_left_operand', return_value='ten'))
            stack.enter_context(patch('__main__.random_operator', return_value='/'))
            stack.enter_context(patch('__main__.random_right_operand', return_value=5))

            actual = calculation()

        expected = 2
        self.assertEqual(actual, expected)


def random_left_operand():
    choices = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'nine', 'ten']

    return random.choice(choices)


def random_right_operand():
    return random.randint(1, 10)


def random_operator():
    operators = ['+', '-', '*', '/']

    return random.choice(operators)


def mapping_number(str_number):
    mappings = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten':10
    }

    return mappings[str_number]

def calculation():
    left_operand = mapping_number(random_left_operand())
    right_operand = random_right_operand()

    operator = random_operator()
    result = {
        '+': left_operand + right_operand,
        '-': left_operand - right_operand,
        '*': left_operand * right_operand,
        '/': round(left_operand / right_operand)
    }

    #This is a magic if you use eval funtion
    #eval(str(left_operand) + operator + str(right_operand))

    return result[operator]

if __name__ == '__main__':
    unittest.main()
