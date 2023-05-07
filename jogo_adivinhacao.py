import random

print("******************")
print("Bem vindo ao jogo!")
print("******************")

numero_secreto = random.randint(1, 100)

nivel = input("Selecione o nível -  (1)Facil (2)Medio (3)Dificil: ")

converter_nivel_em_nume_de_tentativas = {
    '1' : 15,
    '2' : 10,
    '3' : 5
}

converter_nivel_em_saldo_de_pontos = {
    '1' : 150,
    '2' : 70,
    '3' : 20
}

tentativas = converter_nivel_em_nume_de_tentativas[nivel]
saldo_de_pontos = converter_nivel_em_saldo_de_pontos[nivel]

def declarar_vitoria():
    print("Parabéns, você acertou o número secreto!")
    print("E fez {} pontos".format(saldo_de_pontos))
    print("-------------------------------")
    print("            ___________         ")
    print("           '._==_==_=_.'        ")
    print("           .-\\:      /-.       ")
    print("          | (|:.     |) |       ")
    print("           '-|:.     |-'        ")
    print("             \\::.    /         ")
    print("              '::. .'           ")
    print("                ) (             ")
    print("              _.' '._           ")
    print("             '-------'          ")

def declarar_derrota():
    print("Você perdeu! Fim da linha pra você!")
    print("----------------------------------")
    print("      ──▄────▄▄▄▄▄▄▄────▄───      ")
    print("      ─▀▀▄─▄█████████▄─▄▀▀──      ")
    print("      ─────██─▀███▀─██──────      ")
    print("      ───▄─▀████▀████▀─▄────      ")
    print("      ─▀█────██▀█▀██────█▀──      ")    

for rodada in range(1, tentativas + 1):

    chute = int(input(f"Tentativa nº {rodada} de {tentativas}\nDigite um numero: "))

    acertou = chute == numero_secreto
    chutou_para_baixo = chute < numero_secreto
    chutou_para_cima = chute > numero_secreto
    tentativas_acabaram = rodada == tentativas
    desvio = abs(numero_secreto - chute)
    saldo_de_pontos -= desvio
    saldo_de_pontos_insuficiente = saldo_de_pontos <= 0

    if (saldo_de_pontos_insuficiente):
        print("Seus pontos acabaram! {} pontos".format(saldo_de_pontos))
        declarar_derrota()
        break

    if (acertou):
        declarar_vitoria()
        break

    elif(tentativas_acabaram):
        print("Suas tentativas acabaram!")
        declarar_derrota()

    elif(chutou_para_baixo):
        print("Você errou! Tente um maior!")
        print("----------------------------")
    elif(chutou_para_cima):
        print("Você errou! Tente um menor!")
        print("----------------------------")
    


# Este é um jogo de adivinhação de números em que o jogador precisa adivinhar um número secreto entre 1 e 100 em um número limitado de tentativas. O número máximo de tentativas é determinado pelo nível selecionado pelo jogador.

# Ao iniciar o jogo, o programa seleciona um número aleatório entre 1 e 100 como o número secreto. O jogador deve então digitar um número para tentar adivinhar o número secreto. Após cada tentativa, o programa informa ao jogador se o número que ele digitou é maior ou menor que o número secreto.

# O jogo possui três níveis de dificuldade: fácil, médio e difícil. O nível selecionado determina o número máximo de tentativas e o saldo de pontos disponível para o jogador. O nível fácil permite 15 tentativas e dá ao jogador 150 pontos para começar. O nível médio permite 10 tentativas e dá ao jogador 70 pontos para começar. O nível difícil permite 5 tentativas e dá ao jogador 20 pontos para começar.

# A cada tentativa, o jogador perde pontos com base na distância entre o número que ele digitou e o número secreto. Se o jogador ficar sem pontos antes de adivinhar o número secreto, ele perde o jogo. Se o jogador adivinhar o número secreto dentro do número máximo de tentativas, ele vence o jogo e com a pontuação restante. Se o jogador não adivinhar o número secreto dentro do número máximo de tentativas, ele perde o jogo.

# O jogo é uma ótima maneira de praticar conceitos básicos de programação em Python, como estruturas de repetição, condicionais e funções.
