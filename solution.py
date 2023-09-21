import re
from typing import List


def largest_unique_number(
        list_of_ints: List[int]
) -> int:
    frequencies = {}
    result = -1
    for nr in list_of_ints:
        if nr not in frequencies:
            frequencies[nr] = 1
        else:
            frequencies[nr] += 1
    for key, value in frequencies.items():
        if value == 1:
            result = max(result, key)
    return result


def remove_duplicates(
        ll: list
) -> list:
    new_list = []
    for elem in ll:
        if elem not in new_list:
            new_list.append(elem)

    return new_list


def reverse_words(
        sentence: str
) -> str:
    splitted = sentence.split()
    return " ".join(splitted[::-1])


def find_missing_number(
        numbers: List[int]
) -> int:
    """Taking into consideration that there is only ONE missing number"""
    for nr in range(1, numbers[-1] + 1):
        if nr not in numbers:
            return nr
    return -1


def is_anagram(
        first: str,
        second: str
) -> bool:
    if len(first) != len(second):
        return False
    map = {}
    for char in first:
        if char not in map:
            map[char] = 1
        else:
            map[char] += 1
    for char in second:
        if char in map:
            map[char] -= 1
        else:
            return False

    return all(v == 0 for v in map.values())


def validate_palindrome(
        string: str
) -> bool:
    pattern = re.compile(r'\W')
    s = re.sub(pattern, '', string)
    return s == s[::-1]


def prime_factors(
        nr: int
) -> List[int]:
    i = 2
    factors = []
    while i <= nr:
        if (nr % i) == 0:
            factors.append(i)
            nr = nr / i
        else:
            i = i + 1
    return factors


def count_words(
        sentence: str
) -> dict:
    frequencies = {}
    for word in sentence.split():
        if word not in frequencies:
            frequencies[word] = 1
        else:
            frequencies[word] += 1
    return frequencies


def matrix_transpose(
        matrix: List[List]
) -> List[List] or IndexError:
    try:
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    except IndexError as e:
        return -1


def binary_search(
        sorted_list: List[int],
        target_number: int
) -> int:
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (high + low) // 2
        if sorted_list[mid] < target_number:
            low = mid + 1
        elif sorted_list[mid] > target_number:
            high = mid - 1
        else:
            return mid
    return -1

