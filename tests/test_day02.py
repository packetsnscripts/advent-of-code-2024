import pytest

from src.day02.solution import safe, is_decreasing


@pytest.fixture
def test_levels():
    level1 = [7, 6, 4, 2, 1]
    level2 = [1, 2, 7, 8, 9]
    level3 = [9, 7, 6, 2, 1]
    level4 = [1, 3, 2, 4, 5]
    level5 = [8, 6, 4, 4, 1]
    level6 = [1, 3, 6, 7, 9]
    return level1, level2, level3, level4, level5, level6


def test_safe(test_levels):
    level1, level2, level3, level4, level5, level6 = test_levels
    assert safe(level1) is True
    assert safe(level2) is False
    assert safe(level3) is False
    assert safe(level4) is False
    assert safe(level5) is False
    assert safe(level6) is True


def test_is_decreasing(test_levels):
    level1, level2, level3, level4, level5, level6 = test_levels
    assert is_decreasing(level1) is True
