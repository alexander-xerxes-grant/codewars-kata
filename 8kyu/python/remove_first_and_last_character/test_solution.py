from solution import remove_first_and_last


def test_remove_first_and_last():
    assert remove_first_and_last("eloquent") == "loquen"
    assert remove_first_and_last("country") == "ountr"
    assert remove_first_and_last("person") == "erso"
    assert remove_first_and_last("place") == "lac"
    assert remove_first_and_last("ok") == ""
    assert remove_first_and_last("ooopsss") == "oopss"
