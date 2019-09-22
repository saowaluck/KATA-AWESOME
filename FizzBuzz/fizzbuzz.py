import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_input_3_should_be_fizz(self):
        input = 3

        actual = fizzbuzz(input)

        expected = 'fizz'
        self.assertEqual(actual, expected)

    def test_input_6_should_be_fizz(self):
        input = 6

        actual = fizzbuzz(input)

        expected = 'fizz'
        self.assertEqual(actual, expected)

    def test_input_5_should_be_buzz(self):
        input = 5

        actual = fizzbuzz(input)

        expected = 'buzz'
        self.assertEqual(actual, expected)

    def test_input_10_should_be_buzz(self):
        input = 10

        actual = fizzbuzz(input)

        expected = 'buzz'
        self.assertEqual(actual, expected)

    def test_input_15_should_be_fizzbuzz(self):
        input = 15

        actual = fizzbuzz(input)

        expected = 'fizzbuzz'
        self.assertEqual(actual, expected)

    def test_input_30_should_be_fizzbuzz(self):
        input = 30

        actual = fizzbuzz(input)

        expected = 'fizzbuzz'
        self.assertEqual(actual, expected)

    def test_input_7_should_be_itself(self):
        input = 7

        actual = fizzbuzz(input)

        expected = 7
        self.assertEqual(actual, expected)

    def test_input_1_should_be_itself(self):
        input = 1

        actual = fizzbuzz(input)

        expected = 1
        self.assertEqual(actual, expected)


def fizzbuzz(input):
    if input % 15 == 0:
        return 'fizzbuzz'
    elif input % 3 == 0:
        return 'fizz'
    elif input % 5 == 0:
        return 'buzz'
    else:
        return input


if __name__ == '__main__':
    unittest.main()
