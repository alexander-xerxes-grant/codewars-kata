from solution import get_index


def test_get_index():

    assert (
        get_index("The sunset sets at twelve o' clock.")
        == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    )
    assert get_index("abc") == "1 2 3"
    assert get_index("a.b.c") == "1 2 3"
