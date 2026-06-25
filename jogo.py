from jogadores.jogadorhumano import JogadorHumano
from jogadores.jogadorbot import JogadorBot
from rich.table import Table
from rich.console import Console

class Jogo:
    """Gerencia o fluxo principal e as regras de pontuação de uma partida de Jokenpô.

    Esta classe controla o loop do jogo, solicita as jogadas dos participantes,
    computa quem venceu cada rodada e exibe o placar estilizado no terminal.
    """

    def __init__(self, jogador_humano, jogador_bot):
        self.jogador_humano = jogador_humano
        self.jogador_bot = jogador_bot
        self.console = Console()


    def iniciar_partida(self) -> None:
        """Inicia o loop principal do jogo e o mantém rodando até alguém atingir 30 pontos."""
        self.exibir_placar(self.jogador_bot) # iniciar mostrando o placar!

        while True:
            # iniciando as escolhas do bot e do humano.
            iniciando_humano = self.jogador_humano.escolher_jogada() 
            iniciando_bot = self.jogador_bot.escolher_jogada()

            # iniciando a luta e vendo quem venceu.
            resultado = iniciando_humano.contra(iniciando_bot)

            # Adicionamos cores e espaçamento aqui para desbugar o visual
            if resultado == "vitoria":
                self.jogador_humano.pontuacao += 10
                self.console.print("\n🎉 [bold green]Você ganhou +10 pontos![/bold green]")
            elif resultado == "derrota":
                self.jogador_bot.pontuacao += 10
                self.console.print("\n😢 [bold red]Você perdeu! O adversário ganhou +10 pontos.[/bold red]")
            else:
                self.console.print("\n🤝 [bold yellow]Foi empate! Ninguém pontua.[/bold yellow]")

            if self.jogador_humano.pontuacao == 30 or self.jogador_bot.pontuacao == 30:
                self.console.print("\n🏆 [bold light_blue]Jogo acabou! Alguém atingiu o limite de 30 pontos![/bold light_blue]")
                self.exibir_placar(self.jogador_bot)
                break
            else:
                self.exibir_placar(self.jogador_bot)

        self.fim_de_jogo() # finalizando jogo!

    def exibir_placar(self, adversario) -> None:
        """Gera e exibe uma tabela estilizada contendo as pontuações atuais."""
        # Cria a estrutura da tabela
        tabela = Table(title="🏆 PLACAR ATUAL 🏆", style="bold cyan")
            
        # Define as colunas
        tabela.add_column("Jogador", justify="center", style="bold white", width=20)
        tabela.add_column("Pontuação", justify="center", style="bold yellow", width=15)
            
        # Adiciona as linhas com os dados atuais dos jogadores
        tabela.add_row(self.jogador_humano.nome, f"{self.jogador_humano.pontuacao} pts")
        tabela.add_row(adversario.nome, f"{adversario.pontuacao} pts")
            
        # Linha em branco para separar visualmente no terminal
        self.console.print("\n")
        self.console.print(tabela)

    def fim_de_jogo(self):
        """Exibe o resultado final da partida de forma estilizada."""
        self.console.print("\n[bold purple]---------------- FIM DE JOGO ----------------[/bold purple]")
        self.exibir_placar(self.jogador_bot)
        
        if self.jogador_humano.pontuacao > self.jogador_bot.pontuacao:
            self.console.print(f"\n🥇 [bold green]{self.jogador_humano.nome} VENCEU A PARTIDA![/bold green] 🎉\n")
        else:
            self.console.print(f"\n🤖 [bold red]{self.jogador_bot.nome} VENCEU A PARTIDA![/bold red] Mais sorte na próxima!\n")
