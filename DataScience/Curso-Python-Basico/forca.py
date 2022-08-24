def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    palavra_secreta = palavra_secreta.strip().upper()
    
    letras_acertadas = ["_","_","_","_","_","_"]
    print("Palavra:",letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    chances = 6
    acertou_letra = False


    while(not enforcou and not acertou):
        chute = input("Qual letra?\n")
        chute = chute.strip().upper()

        index = 0

        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
                acertou_letra = True
                               
            index += 1

        if (acertou_letra): 
            print("A palavra possui a letra {}!".format(chute))
            acertou_letra = False
        else:
            print("Errou! Você tem mais {} tentativa(s).".format(chances-erros))
            erros += 1
            if (erros == chances):
                enforcou = True
        
        acertou = "_" not in letras_acertadas
        print("\n",letras_acertadas)
    
    if(acertou):
        print("Você ganhou!")
        
    else:
        print("\nVocê foi enforcado!")

    print("\n***********Fim do jogo***********")

if(__name__ == "__main__"):
    jogar()
 