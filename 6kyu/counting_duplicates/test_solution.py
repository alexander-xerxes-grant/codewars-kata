from solution import count_duplicates


def test_count_duplicates():

    assert count_duplicates("abcde") == 0
    assert count_duplicates("aabbcde") == 2
    assert count_duplicates("aabBcde") == 2
    assert count_duplicates("indivisibility") == 1
    assert count_duplicates("Indivisibilities") == 2
    assert count_duplicates("aA11") == 2
    assert count_duplicates("ABBA") == 2
