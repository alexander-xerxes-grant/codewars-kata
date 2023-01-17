from solution import find_smallest_int


def test_find_smallest_int():
    assert find_smallest_int([34, 15, 88, 2]) == 2
    assert find_smallest_int([34, -345, -1, 100]) == -345
