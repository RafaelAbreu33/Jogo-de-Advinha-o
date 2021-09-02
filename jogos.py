import forca
import adivinhacao

def escolhe():

    print("**")
    print("**Escolha seu jogo!**")
    print("**")

    print("(1) Forca (2) advinhação")
    jogo = int(input("Qual o jogo?"))

    if(jogo == 1):
        print("**jogando Forca!**")
        forca.jogar()
    elif(jogo == 2):
        print("***jogando advinhação**")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe()