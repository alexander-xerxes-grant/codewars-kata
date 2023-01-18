from solution import get_sum


def test_get_sum():

    assert get_sum(1, 0) == 1
    assert get_sum(1, 2) == 3
    assert get_sum(0, 1) == 1
    assert get_sum(-1, 0) == -1
    assert get_sum(1, 1) == 1
    assert get_sum(-1, 2) == 2
