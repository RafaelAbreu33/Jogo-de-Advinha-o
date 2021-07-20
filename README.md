import random


print("***********************************")
print("Bem vindo ao meu jogo de advinhação")
print("***********************************")


numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
rodada = 1
pontos = 1000
reiniciar = 1

while reiniciar:

    print("Qual o nível da dificuldade: ")
    print("(1) Fácil (2) Médio (3) Difícil")

    nível = int(input("Defina o nível:" ))

    if(nível == 1 ):
        total_de_tentativas = 20
    elif(nível == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range (1, total_de_tentativas + 1):

        print("tentativa {} de {}".format(rodada, total_de_tentativas ))
        chute = input("Você deve digitar um número de 1 a 100: ")
        print("Você digitou ",chute)
        chute = int(chute)

        if(chute < 1 or chute > 100 ):
            print("Você deve digitar um número de 1 a 100: ")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if(acertou):
            print("Você acertou e fez {} pontos ".format(pontos))
            break
        else:
            if(maior):
                print("Você errou, o seu numero secreto é menor que {}".format(chute))
            if(menor):
                print("Você errou, o seu numero secreto é maior que {}".format(chute))
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("seu número secreto era: {}".format(numero_secreto))
    print("deseja jogar novamente?")


    reiniciar = int(input("digite 1 para SIM ou 0 para NÃO:"))
print("fim")
