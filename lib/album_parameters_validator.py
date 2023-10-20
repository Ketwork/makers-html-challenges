class AlbumParameterValidator:
    
    def __init__(self, title, release_year):
        self.title = title
        self.release_year = release_year

    def is_valid(self):
        if self.title is None or self.title == "":
            return False
        if self.release_year is None:
            return False
        if not self.release_year.isdigit():
            return False
        return True