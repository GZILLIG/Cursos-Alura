# Importa a biblioteca random para ser possivel usa-la
import random

# Insere o programa inteiro numa função, para poder ser chamada em outro arquivo python
def jogar():

    imprime_mensagem_de_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = cria_grid_underline_palavra(palavra_secreta)
    
    print("\n Sua palavra tem {} letras.".format(len(letras_acertadas)))
    
    #Criação de variáveis globais
    erros = 0
    chances = 8


    while(True): #Cria um loop infinito, até encontrar um break
        chute = pede_chute_para_jogador()

        acertou_letra = verifica_se_letra_esta_na_palavra_secreta(palavra_secreta, letras_acertadas, chute)

        print("\n",letras_acertadas) #exibe a string palavras acertadas
        
        if (acertou_letra): #mensagem de acerto
            print("A palavra possui a letra {}!".format(chute))
            acertou_letra = False
        else: #messagem de erro
            desenha_forca(erros)
            print("Errou! Você tem mais {} tentativa(s).".format(chances-erros))
            erros += 1 #contabiliza o erro
            if (erros == chances):
                break #se as chances se acabarem, sair do While
        
        
        if ("_" not in letras_acertadas):
            break #Se todas as letras foram descobertas, sair do While
        
    
    if("_" not in letras_acertadas):
        imprime_mensagem_vencedor()
                
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("\n***********Fim do jogo***********")

def verifica_se_letra_esta_na_palavra_secreta(palavra_secreta, letras_acertadas, chute):
    index = 0 #inicializa indice de letras
    acertou_letra = False
    for letra in palavra_secreta: #Percorre letra por letra da string 'palavra_secreta'
        if(chute == letra): #verifica se a letra do chute existe naquela posição
            letras_acertadas[index] = letra #Se sim, substituir o '_' no letras acertadas pela letra do chute
            acertou_letra = True #flag para exibir mensagem de acerto, em outro If

        index += 1 #incrementa o indice de letras
    return acertou_letra

def pede_chute_para_jogador():
    chute = input("Qual letra que tentar?\n")
    chute = chute.strip().upper() #limpa e capslock na variavel chute, fornecida pelo usuario
    return chute

def cria_grid_underline_palavra(palavra_secreta):
    return ["_" for letra in palavra_secreta] #Cria uma lista com _ para cada letra da palavra secreta

def carrega_palavra_secreta():
    #abre o arquivo "palavras.txt" e salva na lista sqltxt_palavras
    sqltxt_palavras = open("/home/gabriel/Área de Trabalho/Cursos-Alura/DataScience/Curso-Python-Basico/palavras.txt", "r")
    palavras = [] #Cria uma lista vazia
    
    for linha in sqltxt_palavras: #extrai valor por valor da lista para a string linha
        linha = linha.strip().upper() #limpa e coloca em caixa alta a palavra extraida
        palavras.append(linha) #adiciona a palavra já limpa na lista palavras
        
    sqltxt_palavras.close() #fecha o arquivo palavras.txt
    
    index_palavra_secreta = random.randrange(0,len(palavras)) #gera um valor aleatorio entre 0 e numero de items da lista palavras
        
    palavra_secreta = palavras[index_palavra_secreta] #transfere a palavra selecionada para palavra_secreta
    return palavra_secreta

def imprime_mensagem_de_abertura():
        print("*********************************")
        print("***Bem vindo ao jogo da Forca!***")
        print("*********************************")
        
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
        
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
if(__name__ == "__main__"): #Como inserimos o programa todo dentro de uma função, ele só é executado quando chamada. Este if chama a função 'jogar()' caso abrirmos o arquivo forca.py diretamente.
    jogar()


