from lib.album_parameters_validator import AlbumParameterValidator

"""
With valid title and year
It is valid
"""
def test_is_valid():
    validator = AlbumParameterValidator("My Title", "1990")
    assert validator.is_valid() == True

"""
With valid title and year
It is valid
"""
def test_is_not_valid_with_bad_title():
    validator_1 = AlbumParameterValidator("", "1990")
    assert validator_1.is_valid() == False
    validator_2 = AlbumParameterValidator(None, "1990")
    assert validator_2.is_valid() == False

"""
With non-integer-convertible-string release year
It is not valid
"""
def test_is_not_valid_with_bad_release_year():
    validator_1 = AlbumParameterValidator("My Title", "")
    assert validator_1.is_valid() == False
    validator_2 = AlbumParameterValidator("My Title", None)
    assert validator_2.is_valid() == False
    validator_3 = AlbumParameterValidator("My Title", "fred")
    assert validator_3.is_valid() == False