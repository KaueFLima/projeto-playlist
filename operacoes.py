from biblioteca import Biblioteca
from fila import Fila
from utils import (
    cabecalho, exibir_musica, menu_humor,
    ler_inteiro, ler_texto, classificar_bpm,
)



def op_adicionar(biblioteca: Biblioteca) -> None:
    cabecalho("Adicionar Música")

    titulo = ler_texto("  Título  : ")
    if titulo is None:
        return
    artista = ler_texto("  Artista : ")
    if artista is None:
        return
    genero = ler_texto("  Gênero  : ")
    if genero is None:
        return
    bpm = ler_inteiro("  BPM     : ", minimo=1)
    if bpm is None:
        return

    musica = biblioteca.inserir(titulo, artista, genero, bpm)
    print(f"\n Música adicionada com ID {musica.id}.")



def op_remover(biblioteca: Biblioteca) -> None:
    cabecalho("Remover Música")

    id_ = ler_inteiro("  ID da música: ", minimo=1)
    if id_ is None:
        return

    if biblioteca.remover_por_id(id_):
        print(f"Música ID {id_} removida com sucesso.")
    else:
        print(f" Nenhuma música encontrada com ID {id_}.")



def op_buscar(biblioteca: Biblioteca) -> None:
    cabecalho("Buscar Música")
    print("  1 — Buscar por ID")
    print("  2 — Buscar por título")
    opcao = input("  Escolha: ").strip()

    musica = None
    if opcao == "1":
        id_ = ler_inteiro("  ID: ", minimo=1)
        if id_ is not None:
            musica = biblioteca.buscar_por_id(id_)
    elif opcao == "2":
        titulo = ler_texto("  Título: ")
        if titulo is not None:
            musica = biblioteca.buscar_por_titulo(titulo)
    else:
        print("Opção inválida.")
        return

    if musica:
        print("\n  Música encontrada:")
        exibir_musica(musica)
    else:
        print("Música não encontrada.")



def op_listar(biblioteca: Biblioteca) -> None:
    cabecalho("Biblioteca Completa")

    if biblioteca.tamanho == 0:
        print("A biblioteca está vazia.")
        return

    for musica in biblioteca.listar():
        exibir_musica(musica)



def op_montar_filas(biblioteca: Biblioteca, humores: dict) -> None:
    cabecalho("Montar Filas de Reprodução por Humor")

    for cfg in humores.values():
        cfg["fila"].limpar()

    total = 0
    for musica in biblioteca.listar():
        chave = classificar_bpm(musica.bpm)
        humores[chave]["fila"].enqueue(musica)
        total += 1

    print(f"Filas remontadas com {total} música(s).")
    for chave in ("1", "2", "3", "4"):
        cfg = humores[chave]
        print(f"    • {cfg['nome']:8s} ({cfg['desc']:13s}): "
              f"{cfg['fila'].tamanho} música(s)")



def op_reproduzir(humores: dict, historico: Fila) -> None:
    cabecalho("Reproduzir Próxima Música")
    menu_humor(humores)
    chave = input("  Fila de humor: ").strip()

    if chave not in humores:
        print("Opção inválida.")
        return

    fila = humores[chave]["fila"]
    if fila.esta_vazia():
        print(f"  ✗ A fila '{humores[chave]['nome']}' está vazia.")
        return

    musica = fila.dequeue()
    historico.enqueue(musica)
    print("\n  ▶ Reproduzindo agora:")
    exibir_musica(musica)



def op_exibir_fila(humores: dict) -> None:
    cabecalho("Exibir Fila de Humor")
    menu_humor(humores)
    chave = input("  Fila de humor: ").strip()

    if chave not in humores:
        print("Opção inválida.")
        return

    cfg = humores[chave]
    fila = cfg["fila"]
    bpm_max = cfg["bpm_max"] if cfg["bpm_max"] < 99999 else "+"
    print(f"\n  Fila: {cfg['nome']} — {cfg['desc']} "
          f"(BPM {cfg['bpm_min']}–{bpm_max}) "
          f"— {fila.tamanho} música(s)")

    if fila.esta_vazia():
        print("  (fila vazia)")
        return

    for i, musica in enumerate(fila.listar(), 1):
        print(f"\n  [{i}]")
        exibir_musica(musica)


def op_historico(historico: Fila) -> None:
    cabecalho("Histórico de Reproduções")

    if historico.esta_vazia():
        print("  Nenhuma música reproduzida ainda.")
        return

    for i, musica in enumerate(historico.listar(), 1):
        print(f"\n  [{i}]")
        exibir_musica(musica)

def op_estatisticas(biblioteca: Biblioteca, humores: dict, historico: Fila) -> None:
    cabecalho("Estatísticas")

    print(f"  Total na biblioteca          : {biblioteca.tamanho}")
    print()
    for chave in ("1", "2", "3", "4"):
        cfg = humores[chave]
        print(f"  Fila {cfg['nome']:8s} ({cfg['desc']:13s}): "
              f"{cfg['fila'].tamanho} música(s)")
    print()
    print(f"  Total de músicas reproduzidas: {historico.tamanho}")
