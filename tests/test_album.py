from lib.album import Album


"""
Album constructs with an id, title, release_year & artist_id
"""
def test_album_constructs():
    album = Album(1, "Test Album", 1984, 1)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == 1984
    assert album.artist_id == 1

"""
We can format artists to strings nicely
"""
def test_album_format_nicely():
    album = Album(1, "Test Album", 1984, 1)
    assert str(album) == "Album(1, Test Album, 1984, 1)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_artists_are_equal():
    album_1 = Album(1, "Test Album", 1984, 1)
    album_2 = Album(1, "Test Album", 1984, 1)
    assert album_1 == album_2
