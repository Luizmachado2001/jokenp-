from jogador import Jogador
import random

from jogada import Jogada

class JogadorBot(Jogador):
    """Representa um jogador controlado pelo computador.

    Esta classe herda de Jogador e automatiza as decisões de jogada
    utilizando escolhas aleatórias.
    """

    def escolher_jogada(self) -> Jogada:
        """Seleciona uma jogada aleatória entre as opções válidas do jogo.

        Returns:
            Jogada: O objeto contendo a opção validada e formatada.
        """
        opcoes = ["pedra", "papel", "tesoura"]
        jogada_escolhida = random.choice(opcoes)

        return Jogada(jogada_escolhida, self.nome)