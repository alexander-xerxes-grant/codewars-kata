from solution import is_isogram


def test_is_isogram():
    assert is_isogram("Dermatoglyphics") == True
    assert is_isogram("isogram") == True
    assert is_isogram("aba") == False, "same chars may not be adjacent"
    assert is_isogram("moOse") == False, "same chars may not be same case"
    assert is_isogram("isIsogram") == False
    assert is_isogram("") == True, "an empty string is a valid isogram"
