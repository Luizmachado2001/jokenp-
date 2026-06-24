from jogadores.jogadorhumano import JogadorHumano
from jogadores.jogadorbot import JogadorBot

class Jogo:
    def __init__(self, jogador_humano, jogador_bot):
        self.jogador_humano = jogador_humano
        self.jogador_bot = jogador_bot


    def iniciar_partida(self) -> None:

        self.exibir_placar(self.jogador_bot) # iniciar mostrando o placar!

        # iniciando as escolhas do bot e do humano.
        iniciando_humano = self.jogador_humano.escolher_jogada() 
        iniciando_bot = self.jogador_bot.escolher_jogada()

        # iniciando a luta e vendo que venceu.
        resultado = iniciando_humano.contra(iniciando_bot)

        if resultado == "vitoria":
            self.jogador_humano.pontuacao += 10
            print("você ganhou 10 pontos")
        elif resultado == "derrota":
            self.jogador_bot.pontuacao += 10
            print("você perdeu e adversario ganhou 10 pontos")
        else:
            print("foi empate")
        
        self.exibir_placar(self.jogador_bot)



    def exibir_placar(self, adversario) -> str:
        print(f"{self.jogador_humano.nome} pontuação {self.jogador_humano.pontuacao}")
        print(f"{adversario.nome} pontuação: {adversario.pontuacao}")