
from fila import Fila
from biblioteca import Biblioteca
from operacoes import (
    op_adicionar, op_remover, op_buscar, op_listar,
    op_montar_filas, op_reproduzir, op_exibir_fila,
    op_historico, op_estatisticas,
)

MENU = """
╔══════════════════════════════════════════════════╗
║            GERENCIADOR DE MÚSICAS                ║
╠══════════════════════════════════════════════════╣
║  1  Adicionar música à biblioteca                ║
║  2  Remover música da biblioteca                 ║
║  3  Buscar música                                ║
║  4  Listar biblioteca completa                   ║
║  5  Montar filas de reprodução por humor         ║
║  6  Reproduzir próxima                           ║
║  7  Exibir fila de humor                         ║
║  8  Exibir histórico de reproduções              ║
║  9  Estatísticas                                 ║
║  0  Sair                                         ║
╚══════════════════════════════════════════════════╝
"""


def _inicializar_humores() -> dict:
    return {
        "1": {"fila": Fila("Relaxar"),  "nome": "Relaxar",  "desc": "tranquilo",    "bpm_min": 0,   "bpm_max": 80},
        "2": {"fila": Fila("Focar"),    "nome": "Focar",    "desc": "concentração", "bpm_min": 81,  "bpm_max": 120},
        "3": {"fila": Fila("Animar"),   "nome": "Animar",   "desc": "agitado",      "bpm_min": 121, "bpm_max": 160},
        "4": {"fila": Fila("Treinar"),  "nome": "Treinar",  "desc": "intenso",      "bpm_min": 161, "bpm_max": 99999},
    }


def main() -> None:
    biblioteca = Biblioteca()
    historico = Fila("Histórico")
    humores = _inicializar_humores()

    acoes = {
        "1": lambda: op_adicionar(biblioteca),
        "2": lambda: op_remover(biblioteca),
        "3": lambda: op_buscar(biblioteca),
        "4": lambda: op_listar(biblioteca),
        "5": lambda: op_montar_filas(biblioteca, humores),
        "6": lambda: op_reproduzir(humores, historico),
        "7": lambda: op_exibir_fila(humores),
        "8": lambda: op_historico(historico),
        "9": lambda: op_estatisticas(biblioteca, humores, historico),
    }

    while True:
        print(MENU)
        opcao = input("  Opção: ").strip()

        if opcao == "0":
            break
        elif opcao in acoes:
            acoes[opcao]()
        else:
            print(" Opção inválida. Tente novamente.")

        input("\n  Pressione Enter para continuar")


if __name__ == "__main__":
    main()
