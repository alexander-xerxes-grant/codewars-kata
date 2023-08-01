from solution import find_multiples


def test_find_multiples():

    assert find_multiples(10) == 23
    assert find_multiples(0) == 0
    assert find_multiples(4) == 3
    assert find_multiples(6) == 8
    assert find_multiples(16) == 60
