import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/goodbye')
def get_goodbye():
    return render_template("goodbye.html")

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html", albums=albums)

@app.route('/albums/<int:id>')
def get_single_album(id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)

    album = album_repository.find(id)
    artist = artist_repository.find(album.artist_id)
    
    return render_template("albums/show.html", album=album, artist=artist)

@app.route('/artists/<int:id>')
def get_single_artist(id):
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)

    artist = artist_repository.find(id)

    return render_template("artists/show.html", artist=artist)

@app.route('/artists')
def get_all_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    
    artists = repository.all()

    return render_template("artists/index.html", artists=artists)

@app.route('/albums/new')
def get_album_new():
    return render_template("albums/new.html")

@app.route('/albums', methods=["POST"])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    title = request.form['title']
    release_year = int(request.form['release_year'])
    album = Album(None, title, release_year, 1)

    repository.create(album)
    return redirect(f"albums/{album.id}")


# == Previous project Routes Here ==

# @app.route('/albums', methods=['POST'])
# def post_album():
#     if has_invalid_album_parameters(request.form):
#         return "You need to summit a title, release_year, and artist_id", 400
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     album = Album(
#         None,
#         request.form['title'],
#         request.form['release_year'],
#         request.form['artist_id'])
#     repository.create(album)
#     return '', 200

# def has_invalid_album_parameters(form):
#     return 'title' not in form or \
#         'release_year' not in form \
#         or 'artist_id' not in form

# @app.route('/albums', methods=['GET'])
# def get_albums():
#     connection = get_flask_database_connection(app)
#     respository = AlbumRepository(connection)
#     return "\n".join(
#         f"{album}" for album in respository.all()
#     )

# @app.route('/artists', methods=['GET'])
# def get_all_artist_names():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)

#     return ", ".join([artist.name for artist in repository.all()])

# @app.route('/artists', methods=['POST'])
# def create_artist():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)

#     artist = Artist(
#         None,
#         request.form['name'],
#         request.form['genre'])
#     repository.create(artist)
#     return '', 200

# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
