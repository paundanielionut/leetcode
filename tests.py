import unittest

from solution import largest_unique_number, remove_duplicates, reverse_words, find_missing_number, is_anagram, \
    validate_palindrome, prime_factors, count_words, matrix_transpose, binary_search


class SolutionTests(unittest.TestCase):
    def test_largest_unique_number_empty(self):
        ll = []
        expected = -1
        result = largest_unique_number(ll)
        self.assertEqual(result, expected)

    def test_largest_unique_number(self):
        ll = [1, 2, 5, 6, 7, 8, 9, 9]
        expected = 8
        result = largest_unique_number(ll)
        self.assertEqual(result, expected)

    def test_remove_duplicates(self):
        ll = [1, 2, 2, 3]
        expected = [1, 2, 3]
        result = remove_duplicates(ll)
        self.assertEqual(result, expected)

    def test_reverse_words(self):
        ll = "asd sdf dfg fgh"
        expected = "fgh dfg sdf asd"
        result = reverse_words(ll)
        self.assertEqual(result, expected)

    def test_find_missing_number(self):
        ll = [1, 2, 4, 5]
        expected = 3
        result = find_missing_number(ll)
        self.assertEqual(result, expected)

    def test_find_missing_number_first(self):
        ll = [2, 3, 4, 5]
        expected = 1
        result = find_missing_number(ll)
        self.assertEqual(expected, result)

    def test_is_anagram(self):
        first = "listen"
        second = "silent"
        expected_result = True
        result = is_anagram(first, second)
        self.assertEqual(expected_result, result)

    def test_is_not_anagram(self):
        first = "nolisten"
        second = "silent"
        expected_result = False
        result = is_anagram(first, second)
        self.assertEqual(expected_result, result)

    def test_validate_palindrome(self):
        string = "abcba"
        expected_result = True
        result = validate_palindrome(string)
        self.assertEqual(expected_result, result)

    def test_validate_not_palindrome(self):
        string = "abcffba"
        expected_result = False
        result = validate_palindrome(string)
        self.assertEqual(expected_result, result)

    def test_validate_palindrome_ignore_whitespaces(self):
        string = "abc  ba"
        expected_result = True
        result = validate_palindrome(string)
        self.assertEqual(expected_result, result)

    def test_validate_palindrome_ignore_nonalfanumerics(self):
        string = "abc+/@#ba"
        expected_result = True
        result = validate_palindrome(string)
        self.assertEqual(expected_result, result)

    def test_prime_factors(self):
        target_nr = 10
        expected_result = [2, 5]
        result = prime_factors(target_nr)
        self.assertEqual(expected_result, result)

    def test_prime_factors_random_prime(self):
        target_nr = 113098123  # this was chosen by pressing the keyboard randomly :)
        expected_result = [113098123]
        result = prime_factors(target_nr)
        self.assertEqual(expected_result, result)

    def test_count_words(self):
        sentence = "asd asd wwww asd wwww eee eee rrr rrr uu uu uu uu"
        expected_result = {'asd': 3, 'wwww': 2, 'eee': 2, 'rrr': 2, 'uu': 4}
        result = count_words(sentence)
        self.assertEqual(result, expected_result)

    def test_matrix_transpose(self):
        matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        expected_result = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        result = matrix_transpose(matrix)
        self.assertEqual(expected_result, result)

    def test_matrix_transpose_fail_matrix(self):
        matrix = [[1, 1, 1], [2, 2, 2], [3, 3]]
        expected_result = -1
        result = matrix_transpose(matrix)
        self.assertEqual(expected_result, result)

    def test_binary_search(self):
        target_nr = 7
        target_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_result = 6
        result = binary_search(target_array, target_nr)
        self.assertEqual(expected_result, result)

    def test_binary_search_unsorted(self):
        target_nr = 20
        target_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_result = -1
        result = binary_search(target_array, target_nr)
        self.assertEqual(expected_result, result)
