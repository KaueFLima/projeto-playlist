

from musica import Musica


class NodoFila:

    def __init__(self, musica: Musica):
        self.musica: Musica = musica
        self.proximo: "NodoFila | None" = None


class Fila:


    def __init__(self, nome: str = ""):
        self.nome = nome
        self._inicio: NodoFila | None = None
        self._fim: NodoFila | None = None
        self._tamanho: int = 0

    def enqueue(self, musica: Musica) -> None:
        novo = NodoFila(musica)
        if self._fim is None:
            self._inicio = self._fim = novo
        else:
            self._fim.proximo = novo
            self._fim = novo
        self._tamanho += 1

    def dequeue(self) -> Musica | None:
        if self._inicio is None:
            return None
        musica = self._inicio.musica
        self._inicio = self._inicio.proximo
        if self._inicio is None:
            self._fim = None
        self._tamanho -= 1
        return musica

    def limpar(self) -> None:
        self._inicio = self._fim = None
        self._tamanho = 0

    def listar(self):
        atual = self._inicio
        while atual is not None:
            yield atual.musica
            atual = atual.proximo

    @property
    def tamanho(self) -> int:
        return self._tamanho

    def esta_vazia(self) -> bool:
        return self._tamanho == 0
