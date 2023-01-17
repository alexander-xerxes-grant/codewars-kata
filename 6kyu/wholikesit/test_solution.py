from solution import likes


def test_likes():
    assert likes([]) == "no one likes this"
    assert likes(["Peter"]) == "Peter likes this"
    assert likes(["Jacob", "Alex"]) == "Jacob and Alex like this"
    assert likes(["Max", "John", "Mark"]) == "Max, John and Mark like this"
    assert (
        likes(["Alex", "Jacob", "Mark", "Max"]) == "Alex, Jacob and 2 others like this"
    )
    assert (
        likes(["Alex", "Jacob", "Mark", "Max", "John"])
        == "Alex, Jacob and 3 others like this"
    )
    assert (
        likes(["Alex", "Jacob", "Mark", "Max", "John", "Peter"])
        == "Alex, Jacob and 4 others like this"
    )
