import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    
    for linha in sqltxt_palavras:
        linha = linha.strip().upper()
        palavras.append(linha)
        
    sqltxt_palavras.close()
    
    index_palavra_secreta = random.randrange(0,len(palavras))
        
    palavra_secreta = palavras[index_palavra_secreta]
    
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    print("\n Sua palavra tem {} letras.".format(len(letras_acertadas)))

    erros = 0
    chances = 6
    acertou_letra = False


    while(True):
        chute = input("Qual letra que tentar?\n")
        chute = chute.strip().upper()

        index = 0

        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
                acertou_letra = True

            index += 1

        print("\n",letras_acertadas)
        
        if (acertou_letra): 
            print("A palavra possui a letra {}!".format(chute))
            acertou_letra = False
        else:
            print("Errou! Você tem mais {} tentativa(s).".format(chances-erros))
            erros += 1
            if (erros == chances):
                break
        
        
        if ("_" not in letras_acertadas):
            break
        
    
    if("_" not in letras_acertadas):
        print("Você ganhou!")
        
    else:
        print("\nVocê foi enforcado!")
        print("A palavra secreta era",palavra_secreta)

    print("\n***********Fim do jogo***********")

if(__name__ == "__main__"):
    jogar()
