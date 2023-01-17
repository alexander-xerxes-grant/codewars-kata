from solution import find_shortest_word


def test_find_shortest_word():
    assert find_shortest_word("aa abc abc abcd") == 2
    assert find_shortest_word("aab abcd abcd abcd abcd") == 3
    assert find_shortest_word("abcdefg abc abc abc abc abc abc a") == 1
    assert (
        find_shortest_word(
            "abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyzabcdefg"
        )
        == 26
    )
