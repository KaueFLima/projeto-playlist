

class Musica:

    def __init__(self, id_: int, titulo: str, artista: str, genero: str, bpm: int):
        self.id = id_
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def __str__(self) -> str:
        return (f"  ID     : {self.id}\n"
                f"  Título : {self.titulo}\n"
                f"  Artista: {self.artista}\n"
                f"  Gênero : {self.genero}\n"
                f"  BPM    : {self.bpm}")
