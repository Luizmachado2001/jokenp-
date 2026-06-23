class Jogada:
    """Representa a jogada escolhida por um jogador em uma rodada de Jokenpô.

    Esta classe encapsula a escolha (ex: pedra, papel ou tesoura), as regras de 
    vulnerabilidade de cada elemento e a lógica para determinar o vencedor 
    de um confronto contra outra jogada.

    Attributes:
        escolha (str): A opção escolhida pelo jogador (ex: 'pedra', 'papel', 'tesoura').
        nome (str): O nome do jogador que realizou esta jogada.
        regras (dict): Dicionário mapeando qual elemento vence qual (chave vence o valor).
    """

    def __init__(self, escolha="", nome=""):
        """Inicializa uma nova instância da jogada.

        Args:
            escolha (str, optional): A opção escolhida pelo jogador. O padrão é "".
            nome (str, optional): O nome do jogador dono da jogada. O padrão é "".
        """
        self.escolha = escolha
        self.nome = nome

        self.regras = {
            "tesoura": "papel",
            "papel": "pedra",
            "pedra": "tesoura"
        }


    def contra(self, jogada_adversario) -> str:
        """Realiza o confronto desta jogada contra a jogada de um adversário.

        Compara as escolhas ignorando letras maiúsculas ou minúsculas, 
        imprime o resultado do duelo no terminal e futuramente retornará 
        o status do resultado.

        Args:
            jogada_adversario (Jogada): O objeto da jogada realizada pelo oponente.

        Returns:
            str: Uma string indicando o resultado para o dono desta jogada.
                 Nota: O método atualmente realiza apenas prints e precisa 
                 de ajustes futuros para retornar explicitamente os valores.
        """
        escolha_alterado = self.escolha.lower()
        adversario_escolha = jogada_adversario.escolha.lower()

        print(f"{escolha_alterado} vs {jogada_adversario.escolha}")

        if escolha_alterado == "tesoura" and adversario_escolha == "papel":
            print(f"{self.nome} você ganhou")
        elif escolha_alterado == "papel" and adversario_escolha == "pedra":
            print(f"{self.nome} voce ganhou")
        elif escolha_alterado == "pedra" and adversario_escolha == "tesoura":
            print(f"{self.nome} voce ganhou")
        elif escolha_alterado == adversario_escolha:
            print("empate")
        else:
            print(f"{jogada_adversario.nome} ganhou")