

from musica import Musica


class NodoLista:

    def __init__(self, musica: Musica):
        self.musica: Musica = musica
        self.proximo: "NodoLista | None" = None


class Biblioteca:

    def __init__(self):
        self._cabeca: NodoLista | None = None
        self._tamanho: int = 0
        self._proximo_id: int = 1       

    def inserir(self, titulo: str, artista: str, genero: str, bpm: int) -> Musica:
        nova = Musica(self._proximo_id, titulo, artista, genero, bpm)
        self._proximo_id += 1

        novo_nodo = NodoLista(nova)
        if self._cabeca is None:
            self._cabeca = novo_nodo
        else:
            atual = self._cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo

        self._tamanho += 1
        return nova

    def remover_por_id(self, id_: int) -> bool:
        anterior = None
        atual = self._cabeca

        while atual is not None:
            if atual.musica.id == id_:
                if anterior is None:
                    self._cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self._tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo

        return False

    def buscar_por_id(self, id_: int) -> Musica | None:
        atual = self._cabeca
        while atual is not None:
            if atual.musica.id == id_:
                return atual.musica
            atual = atual.proximo
        return None

    def buscar_por_titulo(self, titulo: str) -> Musica | None:
        titulo_lower = titulo.lower()
        atual = self._cabeca
        while atual is not None:
            if atual.musica.titulo.lower() == titulo_lower:
                return atual.musica
            atual = atual.proximo
        return None

    def listar(self):
        atual = self._cabeca
        while atual is not None:
            yield atual.musica
            atual = atual.proximo

    @property
    def tamanho(self) -> int:
        return self._tamanho
