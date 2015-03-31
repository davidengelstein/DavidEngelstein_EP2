#DavidEngelstein
from turtle import * 
import time
import string
t1 = Turtle()
window = Screen() 
window.bgcolor("lightblue")
window.title("Jogo da Forca")

palavras_usadas = [] #lista para onde serão inseridas as palavras usadas
tentativas = [] #lista para onde serão enviadas as letras usadas
erros_total = 0 #para criar a media geral

def forca():  #função que desenha a forca
    t1.ht()
    t1.left(90)  
    t1.forward(400) 
    t1.right(90)  
    t1.forward(150)
    t1.right(90)  
    t1.forward(50) 
    t1.left(90)
    t1.forward(50)
    t1.left(90)
    t1.forward(100)
    t1.left(90)
    t1.forward(250)
    t1.left(90)
    t1.fd(450)
    t1.left(90)
    t1.forward(50)
    t1.penup()
    t1.fd(50)

continuar = 'sim'

while continuar  =='sim': #enquanto o jogador digitar sim, outra forca se inicia
    t1.setheading(0)
    t1.speed(10)  
    t1.penup()      
    t1.setpos(-250,-200)
    t1.hideturtle()
    
    t1.pendown()
    t1.color("black")
    forca()
    letras_chutadas=[] 
    palavras=open("entrada.txt", encoding="utf-8") #abre o aquivo entrada.txt
    leitura=palavras.readlines() #lê o arquivo entrada
    lista_palavras=[] #para onde vão as palavras do arquivo entrda após serem limpas 
    for i in leitura:
        linha=i.strip() #limpa as palavras 
        if linha!="":
            lista_palavras.append(linha) #caso a linha não esteja em branco, 
            #é adicionada a lista lista_palavras 
    from random import choice
    sorteio = choice(lista_palavras)#soreteio das palavras da lista_palavras 
    while sorteio in palavras_usadas: #para não repetir palvras,
    #se a palvra sorteada ja tiver sido usada, o soreteio ocorre de novo
        sorteio = choice(lista_palavras)#sorteia novamente
        
    print(sorteio)
    palavras_usadas.append(sorteio) #adociona o sorteio a lista de palavras usadas 
    sorteio=sorteio.upper()#todas as letras viram maiúsculas
    def desenhar_tracos():#desenha os traços 
        for i in sorteio:
            if i == " ": #se for espaço não desenhe o traço
                t1.penup()
                t1.fd(40)
                    
            else: #se não for espaço desenhe o traço
                t1.pendown()
                t1.fd(30)
                t1.penup()
                t1.fd(10)
                t1.penup
                ht()
    desenhar_tracos() #chama a função que desenha a forca
    
    def cabeca(): #funçaõ que desenha o braço
        t1.penup()
        t1.setpos(-75,150)
        t1.pendown()
        t1.left(180)
        t1.circle(40)
        t1.penup()
    
    def corpo(): #função que desenha o corpo
        t1.penup()
        t1.setpos(-75,70)
        t1.pendown()
        t1.setpos(-75,-100)
        t1.penup()
        
    def perna1(): #função que desenha a perna1
        t1.penup()
        t1.setpos(-75,-100)
        t1.pendown()
        t1.left(45)
        t1.fd(100)
        t1.penup()
        
    def perna2(): #função que desenha a perna2
        t1.penup()
        t1.setpos(-75,-100)
        t1.pendown()
        t1.left(90)
        t1.fd(100)
        t1.penup()
        
    def braco1(): #função que desenha o braco1
        t1.penup()
        t1.setpos(-75,25)
        t1.pendown()
        t1.fd(100)
        t1.penup()
        
    def braco2(): #função que desenha o braco2
        t1.penup()
        t1.setpos(-75,25)
        t1.pendown()
        t1.right(90)
        t1.fd(100)
        t1.penup()
        
    acertos = 0 
    erros = 0 
    while erros<6 and acertos<len(sorteio)-sorteio.count(' '): 
    #quando a palavra ainda não acabou
           
        variavel = window.textinput(" ", "Escolha uma letra:")  
        variavel = variavel.upper() #transforma todas as letras em maiúsculas
        
        if variavel not in letras_chutadas: #
            letras_chutadas.append(variavel)
            found=0
            for i in range(len(sorteio)):
                
                if variavel == sorteio[i]: #se a letra digitada(variavel) for 
                #igual a alguma letra da palavra escreva a letra
                    t1.setpos(-200+i*40,-200)
                    pendown()
                    t1.write (sorteio[i], font='arial, 14')
                    acertos=acertos+1 #adiciona 1 a variavel acertos
                    penup()
                    found=1
                elif variavel == 'A' and sorteio[i] == 'Ã': #faz a equivalencia entre A e Ã
                    #Ao digitar A, o Ã é escrito também
                    t1.setpos(-200+i*40,-200)
                    pendown()
                    t1.write (sorteio[i], font='arial, 14')
                    acertos=acertos+1
                    penup()
                    found=1
                elif variavel == 'E' and sorteio[i] == 'Ê': #faz a equivalencia entre E e Ê
                #Ao digitar E, o Ê também é escrito
                    t1.setpos(-200+i*40,-200)
                    pendown()
                    t1.write (sorteio[i], font='arial, 14') 
                    acertos=acertos+1
                    penup()
                    found=1
                elif variavel == 'I' and sorteio[i] == 'Í': #faz a equivalência entre I e Í
                #Ao digitar I, o Í também é escrito
                    t1.setpos(-200+i*40,-200)
                    pendown()
                    t1.write (sorteio[i], font='arial, 14')
                    acertos=acertos+1
                    penup()
                    found=1
                elif variavel == 'O' and sorteio[i] == 'Ó': 
                #faz a equivalência do O com o Ó. Ao digitar O, o Ó também é escrito
                    t1.setpos(-200+i*40,-200)
                    pendown()
                    t1.write (sorteio[i], font='arial, 14')
                    acertos=acertos+1
                    penup()
                    found=1
                elif variavel == 'O' and sorteio[i] == 'Ô':
                #faz a equivalência do O com o Ô. Ao digitar O, o Ô também é escrito
                    t1.setpos(-200+i*40,-200)
                    pendown()
                    t1.write (sorteio[i], font='arial, 14')
                    acertos=acertos+1
                    penup()
                    found=1
                
                    
            if found==0 and len(variavel)==1 and variavel!=" " and variavel not in string.digits : 
            #se a letra digitada for tiver 1 caractér e ser diferente de espaço, 
            #é valida, mas a letra não esta na palavra
                    erros=erros+1 #adiciona 1 a variavel erro
                    erros_total=erros_total+1 #adiciona 1 a variavel erro_total
                    #para o calculo da média
                    print(erros_total)
                            
                    if erros == 1:
                        cabeca() #chama a função que desenha a cabeça
                    if erros == 2:
                        corpo() #chama a função que desenha o corpo
                    if erros == 3:
                        perna1() #chama a função que desenha a perna1
                    if erros == 4:
                        perna2() #chama a função que desenha a perna2
                    if erros == 5:
                        braco1() #chama a função que desenha a braco1
                    if erros == 6:
                        braco2() #chama a função que desenha a braco2
                        
            if len(variavel)!=1 or variavel==" " or variavel in string.digits : #se a letra digitada(variavel)
            #tiver um número de caracteres diferentes de 1 ou igual a espaço, 
            #escreva que a palavra é inválida
                t2 = Turtle()
                t2.hideturtle()
                t2.write ('letra invalida', font=('arial', 16))
                time.sleep(1.5)
                t2.clear()
                
                    
        else: #se a letra estiver na lista de letras_usadas
            t3 = Turtle()
            t3.hideturtle()
            t3.write ('letra já inserida', font=('arial', 16))
            time.sleep(1.5)
            t3.clear()
            
    if erros>=6: #quando a variavel erros for igual a 6 (boneco for completo)
        t1.penup()
        t1.setpos(0,0)
        t1.pendown()
        t1.write ('VOCE MORREU', font=('arial', 16))#escreve que você morreu
        t1.penup()
        t1.setpos(50,200)
        t1.pendown()
        t1.write ('PLACAR:' + str(erros) + ' erros', font=('arial', 16))
        #escreve o numero de erros naquela rodada
        t1.penup()
        t1.setpos(50,150)
        t1.pendown()
        t1.write ('MÉDIA DE ERROS:' + str((erros_total)/len(palavras_usadas)) + ' erros', font=('arial', 16))
        #digita a media de erros por rodada
        t1.penup()
        

    if acertos == len(sorteio)-sorteio.count(' '):#quando o número de acertos
    #for igual ao número de letras, a palavra estará completa
        t1.penup()
        t1.setpos(0,0)
        t1.pendown()
        t1.write ('PARABÉNS, VOCÊ GANHOU', font=('arial', 16)) #escreve que você ganhou
        t1.penup()
        t1.setpos(50,200)
        t1.pendown()
        t1.write ('PLACAR:' + str(erros) + ' erros', font=('arial', 16))#escreve
        #o número de erros naquela rodada
        t1.penup()
        t1.setpos(50,150)
        t1.pendown()
        t1.write ('MÉDIA DE ERROS:' + str((erros_total)/len(palavras_usadas)) + ' erros', font=('arial', 16))
        #escreve a média de erros em todas as rodadas
        t1.penup()
        

    if len(palavras_usadas)!=len(lista_palavras): #quando o numero de palavras_usadas
    #for diferente do número de palavras da lista_palavras, pergunta se deseja jogar de novo
        continuar = window.textinput("", "VOCÊ QUER JOGAR NOVAMENTE? Digite sim ou nao")
        t1.clear()

    else: #caso o número de palavras da lista palavras_usadas for igual ao número de
    #palavras da lista lista_palavras, o jogo se encerra, pois não sobraram palavras novas.
        continuar = 'nao'
        t1.clear()
        t1.penup()
        t1.setpos(-300,0)    
        t1.write ('VOCÊ TERMINOU O JOGO', font=('arial', 22))#avisa que o jogo terminou
        t1.penup()
        t1.setpos(-300,50)
        t1.pendown()
        t1.write ('MÉDIA DE ERROS:' + str((erros_total)/len(palavras_usadas)) + ' erros', font=('arial', 16))
        #escreve a media de erros de todas as rodadas
        t1.penup()
        
        
exitonclick()    #fecha a janela com um click