from rich import print, inspect
from jogo import Jogo
from jogadores.jogadorhumano import JogadorHumano
from jogadores.jogadorbot import JogadorBot

def main():

    nome = input("Digite seu nome: ")

    # criando os primeiros jogadores
    j1 = JogadorHumano(nome, 0)

    # criando o segundo jogador.
    bot = JogadorBot("Bot", 0)
    
    # criando o jogo, passando os dois objetos!
    jogando = Jogo(j1, bot)
    jogando.iniciar_partida()
    

if __name__ == "__main__":
    main()