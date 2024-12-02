import pytest

from src.day01.solution_1 import occurences, similarity_score, sum_of_diffs


@pytest.fixture
def test_lists():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]
    return list1, list2


def test_sum_of_diffs(test_lists):
    list1, list2 = test_lists
    assert sum_of_diffs(list1, list2) == 11


def test_occurences(test_lists):
    _, list2 = test_lists
    assert occurences(list2) == {3: 3, 4: 1, 5: 1, 9: 1}


def test_similarity_score(test_lists):
    list1, list2 = test_lists
    assert similarity_score(list1, list2) == 31
