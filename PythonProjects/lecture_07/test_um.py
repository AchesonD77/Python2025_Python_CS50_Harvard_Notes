from um import count


def test_basic():
    assert count("hello, um, world") == 1
    assert count("um?") == 1
    assert count("(um)") == 1


def test_case_insensitive():
    assert count("Um, UM! uM?") == 3


def test_not_substrings():
    # 'um' inside larger words should not count
    assert count("yummy album aluminum umami") == 0
    assert count("drum vacuum chrysanthemum") == 0


def test_multiple_with_punctuation():
    assert count("um... well, um, 'um' (um)!") == 4