from abc import ABC, abstractmethod

class Jogador(ABC):
    """Classe abstrata que representa a estrutura base de um jogador.
    Esta classe define os atributos e métodos obrigatórios que todos os
    tipos de jogadores (humanos ou bots) devem possuir no jogo.
    """

    def __init__(self, nome="", pontuacao=0):
        self.nome = nome
        self.pontuacao = pontuacao

    @abstractmethod
    def escolher_jogada(self):
        """Método abstrato para definir a jogada do jogador.

        Deve ser obrigatoriamente implementado pelas classes filhas.
        """
        pass