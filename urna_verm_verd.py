import random
from matplotlib import pyplot as plt
import numpy as np
# import seaborn as sns
# from matplotlib.ticker import MultipleLocator

# listas de contagem
contagem_bolinha_vermelha = []
contagem_bolinha_verde = []

# variáveis
vermelho_10 = 0
vermelho_20 = 0
vermelho_30 = 0
vermelho_40 = 0
vermelho_50 = 0
vermelho_60 = 0
vermelho_70 = 0
vermelho_80 = 0
vermelho_90 = 0
vermelho_100 = 0

verde_10 = 0
verde_20 = 0
verde_30 = 0
verde_40 = 0
verde_50 = 0
verde_60 = 0
verde_70 = 0
verde_80 = 0
verde_90 = 0
verde_100 = 0

eixo_x = np.arange(0, 10, 1)

for k in range(500):
    # Lista da urna
    urna = ["verde", "verde", "verde", "verde", "verde", "vermelho", "vermelho", "vermelho", "vermelho", "vermelho"]

    # lista 50/50 de bolinhas que entram
    # se quiser priveligiar uma cor, basta adicionar nessa lista
    bolinha_in = ["verde", "vermelho", "verde", "vermelho"]

    # Contador
    c = 0

    while len(urna) < 20 and c < 30:

        # quebra o código antes para não dar erro
        if len(urna) == 0:
            break

        # Randomiza a cada loop a urna para simular o embaralhamento da urna
        random.shuffle(urna)
        numero_da_bolinha_sorteada = random.randrange(0, len(urna), 1)
        bolinha_sorteada = urna[numero_da_bolinha_sorteada]

        # Sorteia a bolinha que irá sair
        numero_da_bolinha_out = random.randrange(0, len(urna), 1)
        bolinha_out = urna[numero_da_bolinha_out]

        # Randomizador da Bolinha que entra
        random.shuffle(bolinha_in)
        bolinha_added = bolinha_in[0]

        # quebra pois não há mais bolinhas
        if len(urna) == 0:
            break

        # Se for vermelha vai retirar uma bolinha aleatória
        if bolinha_sorteada == "vermelho":
            if bolinha_out == "vermelho":
                urna.remove("vermelho")
            if bolinha_out == "verde":
                urna.remove("verde")

        # Se for verde vai adicionar uma bolinha aleatória
        elif bolinha_sorteada == "verde":
            if bolinha_added == "vermelho":
                urna.append("vermelho")
            else:
                urna.append("verde")

        # Contador
        c += 1

    # Variáveis da contagem
    bolinhas_verdes = 0
    bolinhas_vermelhas = 0

    # Contagem de bolinhas
    for w in range(len(urna)):
        if urna[w] == "verde":
            bolinhas_verdes = bolinhas_verdes + 1
            if "verde" not in urna:
                bolinhas_verdes = 0
        else:
            bolinhas_vermelhas = bolinhas_vermelhas + 1
            if "vermelho" not in urna:
                bolinhas_vermelhas = 0
        # contagem
    contagem_bolinha_vermelha.append(bolinhas_vermelhas)
    contagem_bolinha_verde.append(bolinhas_verdes)


# contador em porcentagem - vermelho
for j in range(len(contagem_bolinha_vermelha)):
    if 0 <= contagem_bolinha_vermelha[j] <= 2:
        vermelho_10 += 1
    elif 2 < contagem_bolinha_vermelha[j] <= 4:
        vermelho_20 += 1
    elif 4 < contagem_bolinha_vermelha[j] <= 6:
        vermelho_30 += 1
    elif 6 < contagem_bolinha_vermelha[j] <= 8:
        vermelho_40 += 1
    elif 8 < contagem_bolinha_vermelha[j] <= 10:
        vermelho_50 += 1
    elif 10 < contagem_bolinha_vermelha[j] <= 12:
        vermelho_60 += 1
    elif 12 < contagem_bolinha_vermelha[j] <= 14:
        vermelho_70 += 1
    elif 14 < contagem_bolinha_vermelha[j] <= 16:
        vermelho_80 += 1
    elif 16 < contagem_bolinha_vermelha[j] <= 18:
        vermelho_90 += 1
    elif 18 < contagem_bolinha_vermelha[j] <= 20:
        vermelho_100 += 1

# contador em porcentagem - verde
for p in range(len(contagem_bolinha_verde)):
    if 0 <= contagem_bolinha_verde[p] <= 2:
        verde_10 += 1
    elif 2 < contagem_bolinha_verde[p] <= 4:
        verde_20 += 1
    elif 4 < contagem_bolinha_verde[p] < 6:
        verde_30 += 1
    elif 6 < contagem_bolinha_verde[p] <= 8:
        verde_40 += 1
    elif 8 < contagem_bolinha_verde[p] <= 10:
        verde_50 += 1
    elif 10 < contagem_bolinha_verde[p] <= 12:
        verde_60 += 1
    elif 12 < contagem_bolinha_verde[p] <= 14:
        verde_70 += 1
    elif 14 < contagem_bolinha_verde[p] <= 16:
        verde_80 += 1
    elif 16 < contagem_bolinha_verde[p] <= 18:
        verde_90 += 1
    elif 18 < contagem_bolinha_verde[p] <= 20:
        verde_100 += 1

vermelhas = [vermelho_10, vermelho_20, vermelho_30, vermelho_40, vermelho_50,
             vermelho_60, vermelho_70, vermelho_80, vermelho_90, vermelho_100]
verdes = [verde_10, verde_20, verde_30, verde_40, verde_50,
          verde_60, verde_70, verde_80, verde_90, verde_100]

# Plotagem
# sns.set(style="whitegrid")
# fig, (ax1, ax2) = plt.subplots(2, 1)

# primeiro plot - vermelho
# sns.barplot(x=eixo_x, y=contagem_bolinha_vermelha, ax=ax1, color="red", width=0.4)
# ax1.set_title("Quantidade de Vermelhas")
# ax1.set_xlim(0, 100)
# ax1.set_ylim(0, 20)
# ax1.xaxis.set_major_locator(MultipleLocator(10))

# segundo plot - verde
# sns.barplot(x=eixo_x, y=contagem_bolinha_verde, ax=ax2, color="green", width=0.4)
# ax2.set_title("Quantidade de Verdes")
# ax2.set_xlim(0, 100)
# ax2.set_ylim(0, 20)
# ax2.xaxis.set_major_locator(MultipleLocator(10))
# plt.show()
plt.subplot(2, 1, 1)
plt.bar(eixo_x, vermelhas, width=1, color="red")
plt.subplot(2, 1, 2)
plt.bar(eixo_x, verdes, width=1, color="green")
plt.show()

# criar laço e um dicionário para gerar variáveis para criar mais intervalos de porcentagem
