def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    sql_palavras = open("palavras.txt", "r")
    palavras = []
    
    for linha in sql_palavras:
        linha=linha.strip()
        palavras.append(linha)
    
    sql_palavras.close()
    
    print(sql_palavras)
    
    palavra_secreta = "banana"
    palavra_secreta = palavra_secreta.strip().upper()
    
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    print("Sua palavra tem {} letras.".format(len(letras_acertadas)))

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

    print("\n***********Fim do jogo***********")

if(__name__ == "__main__"):
    jogar()
