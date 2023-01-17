from solution import stringer


def test_stringer():
    assert stringer(True) == 'True'
    assert stringer(False) == 'False'