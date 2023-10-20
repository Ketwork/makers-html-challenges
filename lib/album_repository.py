from lib.album import Album

class AlbumRepository:
    
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all albums
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    
    def create(self, album):
        rows = self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s) RETURNING id', [
                                album.title, album.release_year, album.artist_id])
        # print("here!", rows[0])
        album.id = rows[0]['id']
        return None
    
    def find(self, id):
        rows = self._connection.execute(f'SELECT * FROM albums WHERE id={id}')
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])