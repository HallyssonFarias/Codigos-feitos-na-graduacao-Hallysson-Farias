import random
import matplotlib.pyplot as plt


class Tit_For_Tat:
    def __init__(self):
        self.last_opponent_play = None
        self.pontuation = 0

    def estrategia(self):
        if self.last_opponent_play is None:
            play = "defect"
        else:
            play = self.last_opponent_play

        return play

    def salvar_jogada_oponente(self, jogada_oponente):
        self.last_opponent_play = jogada_oponente


class Random_Strat:
    def __init__(self):
        self.pontuation = 0

    def estrategia(self):
        return random.choice(['defect', 'cooperate'])


# Criação dos jogadores
player_1 = Tit_For_Tat()
player_2 = Random_Strat()

# Inicialização das listas de pontuação e rodadas
pontuacao_player_1 = []
pontuacao_player_2 = []
x = []

# Simulação das rodadas
for rounds in range(50):
    play_1 = player_1.estrategia()
    play_2 = player_2.estrategia()

    # Salvar a jogada do oponente para Tit_For_Tat
    player_1.salvar_jogada_oponente(play_2)

    if play_1 == play_2:
        if play_1 == "cooperate":
            player_1.pontuation += 3
            player_2.pontuation += 3
            print(f"player_1 jogou: {play_1} \n player_2 jogou: {play_2}")
        else:
            player_1.pontuation += 1
            player_2.pontuation += 1
            print(f"player_1 jogou: {play_1} \n player_2 jogou: {play_2}")
    else:
        if play_1 == "cooperate":
            player_1.pontuation += 0
            player_2.pontuation += 5
            print(f"player_1 jogou: {play_1} \n player_2 jogou: {play_2}")
        else:
            player_1.pontuation += 5
            player_2.pontuation += 0
            print(f"player_1 jogou: {play_1} \n player_2 jogou: {play_2}")

    # Armazena os dados para o gráfico
    pontuacao_player_1.append(player_1.pontuation)
    pontuacao_player_2.append(player_2.pontuation)
    x.append(rounds + 1)

# Plotagem do gráfico
plt.scatter(x, pontuacao_player_1, color='red', alpha=0.5)
plt.scatter(x, pontuacao_player_2, color='blue', alpha=0.5)
plt.xlabel("Rodadas")
plt.ylabel("Pontuação")
plt.legend(["Tit_For_Tat", "Random_Strat"])
plt.title("Pontuações ao Longo das Rodadas")
plt.show()
