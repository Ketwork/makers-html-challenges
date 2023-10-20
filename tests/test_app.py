from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_goodbye(page, test_web_address):
    page.goto(f"http://{test_web_address}/goodbye")
    strong_tag = page.locator("strong")
    expect(strong_tag).to_have_text("Bye!")

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Doolittle",
        "Surfer Rosa",
    ])

def test_get_album_1(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")

    page.goto(f"http://{test_web_address}/albums/1")
    h1_tags = page.locator("h1")
    release_year_tags = page.locator(".t-release-year")

    expect(h1_tags).to_have_text("Album: Doolittle")
    expect(release_year_tags).to_have_text("Released: 1989")
    

def test_get_album_2(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")

    page.goto(f"http://{test_web_address}/albums/2")
    h1_tags = page.locator("h1")
    release_year_tags = page.locator(".t-release-year")

    expect(h1_tags).to_have_text("Album: Surfer Rosa")
    expect(release_year_tags).to_have_text("Released: 1988")

"""
The page returned by GET /albums should contain a link for each album listed.
It should link to /albums/<id>, where <id> is the corresponding album's id.
That page should then show information about the specific album.
"""
def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text("Album: Surfer Rosa")
    release_year_tag = page.locator('.t-release-year')
    expect(release_year_tag).to_have_text("Released: 1988")

def test_visit_album_show_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")
    page.click("text='Go back to album list'")
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text("Albums")

def test_get_artist_1(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")

    page.goto(f"http://{test_web_address}/artists/1")
    h1_tags = page.locator("h1")
    genre_tag = page.locator(".t-genre")

    expect(h1_tags).to_have_text("Artist: Pixies")
    expect(genre_tag).to_have_text("Genre: Rock")

def test_get_all_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    li_tags = page.locator("li")
    
    expect(li_tags).to_have_text([
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone"
    ])

def test_visit_artist_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Pixies'")
    h1_tag = page.locator('h1')
    genre_tag = page.locator('.t-genre')

    expect(h1_tag).to_have_text("Artist: Pixies")
    expect(genre_tag).to_have_text("Genre: Rock")

# def test_create_album(page, test_web_address, db_connection):
#     page.set_default_timeout(1000) # kept short for testing
#     db_connection.seed("seeds/record_store.sql")
#     page.goto(f"http://{test_web_address}/albums")
#     page.click('text="Add album"')

#     page.fill('input[name=title]', "Test Album")
#     page.fill('input[name=release_year]', "1234")
#     page.click('text="Add Album"')

#     h1_tag = page.locator('h1')
#     expect(h1_tag).to_have_text("Album: Test Album")
#     release_year_tag = page.locator('.t-release-year')
#     expect(release_year_tag).to_have_text("Released: 1234")

def test_validate_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000) # kept short for testing
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click('text="Add Album"') # on show albums page
    page.click('text="Add Album"') # on add albums page

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text(
        "Your submission contains errors: " \
        "Title can't be blank, " \
        "Release year can't be blank"
    )



# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
