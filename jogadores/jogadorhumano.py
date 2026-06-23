from jogador import Jogador
from jogada import Jogada

class JogadorHumano(Jogador):
    """Representa um jogador humano controlado via terminal.

    Esta classe herda de Jogador e gerencia a entrada de dados do usuário,
    garantindo que apenas jogadas válidas sejam aceitas.
    """

    def escolher_jogada(self) -> Jogada:
        """Solicita e valida a jogada do usuário através do console.

        O método permanece em loop até que o usuário digite uma opção válida
        (Pedra, Papel ou Tesoura), tratando espaços extras e variações de caixa.

        Returns:
            Jogada: O objeto contendo a opção validada e formatada.
        """
        possibilidade = ["PEDRA", "PAPEL", "TESOURA"]

        while True:
            jogada = input(str("Escolha [Pedra, Papel, Tesoura]:")).strip()

            if jogada.isalpha() and jogada.upper() in possibilidade:
                break
            else:
                print("opcao invalida!")

        #print(f"{self.nome} você escolheu {jogada}")

        return Jogada(jogada.capitalize(), self.nome)