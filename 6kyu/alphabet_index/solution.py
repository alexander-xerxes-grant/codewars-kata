import string

alphabet = string.ascii_lowercase


def get_index(s):

    s = s.lower()
    return " ".join(
        [str(alphabet.index(letter) + 1) for letter in s if letter.isalpha()]
    )
