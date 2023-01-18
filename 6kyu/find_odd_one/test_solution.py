from solution import find_odd_one


def test_find_odd_one():
    assert find_odd_one([2, 4, 0, 100, 4, 11, 2602, 36]) == 11
    assert find_odd_one([160, 3, 1719, 19, 11, 13, -21]) == 160
