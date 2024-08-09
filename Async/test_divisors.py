import pytest
from Division import get_divisors, process_number, main

def test_get_divisors():
    assert get_divisors(28) == [1, 2, 4, 7, 14, 28]
    assert get_divisors(29) == [1, 29]  # простое число
    assert get_divisors(1) == [1]

def test_process_number():
    assert process_number(28) == [1, 2, 4, 7, 14, 28]
    assert process_number(29) == [1, 29]

def test_main():
    numbers = [28, 29, 30]
    results = main(numbers)
    assert results == [[1, 2, 4, 7, 14, 28], [1, 29], [1, 2, 3, 5, 6, 10, 15, 30]]