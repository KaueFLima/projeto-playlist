
from musica import Musica


LINHA = "─" * 52

def cabecalho(titulo: str) -> None:
    print(f"\n{'═' * 52}")
    print(f"  {titulo}")
    print(f"{'═' * 52}")


def exibir_musica(musica: Musica) -> None:
    print(LINHA)
    print(musica)
    print(LINHA)


def menu_humor(humores: dict) -> None:
    for chave in ("1", "2", "3", "4"):
        cfg = humores[chave]
        bpm_max = cfg["bpm_max"] if cfg["bpm_max"] < 99999 else "+"
        print(f"  {chave} — {cfg['nome']:8s} "
              f"({cfg['desc']:13s}, "
              f"BPM {cfg['bpm_min']}–{bpm_max})")



def ler_inteiro(prompt: str, minimo: int = 1) -> int | None:
    try:
        valor = int(input(prompt).strip())
        if valor < minimo:
            print(f"O valor deve ser ≥ {minimo}.")
            return None
        return valor
    except ValueError:
        print("Entrada inválida — informe um número inteiro.")
        return None


def ler_texto(prompt: str) -> str | None:
    valor = input(prompt).strip()
    if not valor:
        print("O campo não pode ser vazio.")
        return None
    return valor



def classificar_bpm(bpm: int) -> str:
    if bpm <= 80:
        return "1"
    if bpm <= 120:
        return "2"
    if bpm <= 160:
        return "3"
    return "4"
