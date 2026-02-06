from project.album import Album

class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: list[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        a = next((a for a in self.albums if a.name == album_name), None)
        if not a:
            return f"Album {a.name} is not found."
        if a.published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(a)
        return f"Album {a.name} has been removed."

    def details(self) -> str:
        result = f"Band {self.name}\n"
        albums_details = "\n".join(album.details() for album in self.albums)
        return result + albums_details