from src.solution import solution


def test_case_1():
    assert solution([[2, 1, 2], [5, 1, 1]]) == 13


def test_case_2():
    assert solution([[2, 3, 2], [3, 1, 3], [2, 1, 1]]) == 11


def test_case_3():
    assert solution([[3, 3, 3], [5, 4, 2], [2, 1, 2]]) == 193


def test_case_4():
    assert solution([[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]]) == -1
