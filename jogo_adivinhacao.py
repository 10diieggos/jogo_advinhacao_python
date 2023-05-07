import random

def jogar():

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
        '3' : 50
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

if (__name__ == "__main__"):
    jogar()
        
