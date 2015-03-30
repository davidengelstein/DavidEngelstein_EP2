#DavidEngelstein
from turtle import *
import time
t1 = Turtle()
window = Screen() 
window.bgcolor("lightblue")
window.title("Jogo da Forca")



def forca():  
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
palavras_usadas = []
continuar = 'sim'
while continuar  =='sim':
    t1.setheading(0)
    t1.speed(5)  
    t1.penup()      
    t1.setpos(-250,-200)
    t1.hideturtle()
    
    t1.pendown()
    t1.color("black")
    forca()
    letras_chutadas=[]
    palavras=open("entrada.txt", encoding="utf-8")
    leitura=palavras.readlines()
    lista=[]
    for i in leitura:
        linha=i.strip()
        if linha!="":
            lista.append(linha)
    from random import choice
    sorteio = choice(lista)
    while sorteio in palavras_usadas:
        sorteio = choice(lista)
        
    print(sorteio)
    palavras_usadas.append(sorteio)  
    sorteio=sorteio.upper()
    def desenhar_tracos():
        for i in sorteio:
            if i == " ":
                t1.penup()
                t1.fd(40)
                    
            else:
                t1.pendown()
                t1.fd(30)
                t1.penup()
                t1.fd(10)
                t1.penup
                ht()
    desenhar_tracos()
    
    def cabeca():
        t1.penup()
        t1.setpos(-75,150)
        t1.pendown()
        t1.left(180)
        t1.circle(40)
        t1.penup()
    
    def corpo():
        t1.penup()
        t1.setpos(-75,70)
        t1.pendown()
        t1.setpos(-75,-100)
        t1.penup()
        
    def perna1():
        t1.penup()
        t1.setpos(-75,-100)
        t1.pendown()
        t1.left(45)
        t1.fd(100)
        t1.penup()
        
    def perna2():
        t1.penup()
        t1.setpos(-75,-100)
        t1.pendown()
        t1.left(90)
        t1.fd(100)
        t1.penup()
        
    def braco1():
        t1.penup()
        t1.setpos(-75,25)
        t1.pendown()
        t1.fd(100)
        t1.penup()
        
    def braco2():
        t1.penup()
        t1.setpos(-75,25)
        t1.pendown()
        t1.right(90)
        t1.fd(100)
        t1.penup()
    
    acertos = 0
    erros = 0 
    while erros<6 and acertos<len(sorteio)-sorteio.count(' '):
            
        variavel = window.textinput("Nome Janela", "Texto Pergunta")  
        variavel = variavel.upper()
        if variavel not in letras_chutadas:
            letras_chutadas.append(variavel)
            for i in range(len(sorteio)):
                
                if variavel == sorteio[i]:
                    t1.setpos(-200+i*40,-200)
                    pendown()
                    t1.write (sorteio[i], font='arial, 14')
                    acertos=acertos+1
                    penup()
                elif variavel == 'A' and sorteio[i] == 'Ã':
                    t1.setpos(-200+i*40,-200)
                    pendown()
                    t1.write (sorteio[i], font='arial, 14')
                    acertos=acertos+1
                    penup()
                elif variavel == 'E' and sorteio[i] == 'Ê':
                    t1.setpos(-200+i*40,-200)
                    pendown()
                    t1.write (sorteio[i], font='arial, 14')
                    acertos=acertos+1
                    penup()
                elif variavel == 'I' and sorteio[i] == 'Í':
                    t1.setpos(-200+i*40,-200)
                    pendown()
                    t1.write (sorteio[i], font='arial, 14')
                    acertos=acertos+1
                    penup()
                elif variavel == 'O' and (sorteio[i] == 'Ó'or sorteio[i] == 'Ô'):
                    t1.setpos(-200+i*40,-200)
                    pendown()
                    t1.write (sorteio[i], font='arial, 14')
                    acertos=acertos+1
                    penup()
                    
                
                    
            if variavel not in sorteio:
                    erros=erros+1
                    print(erros)
                            
                    if erros == 1:
                        cabeca()
                    if erros == 2:
                        corpo()
                    if erros == 3:
                        perna1()
                    if erros == 4:
                        perna2()
                    if erros == 5:
                        braco1()
                    if erros == 6:
                        braco2()
        else:
            t2 = Turtle()
            t2.write ('letra já inserida', font=('arial', 20))
            time.sleep(1.5)
            t2.clear()
            
    if erros>=6:
        t1.penup()
        t1.setpos(0,0)
        t1.pendown()
        t1.write ('VOCE MORREU', font=('arial', 20))
        t1.penup()        
        
    if acertos == len(sorteio)-sorteio.count(' '):
        t1.penup()
        t1.setpos(0,0)
        t1.pendown()
        t1.write ('VOCE GANHOU', font=('arial', 20))
        t1.penup()

    if len(palavras_usadas)!=len(lista):
        continuar = window.textinput("", "VOCÊ QUER JOGAR NOVAMENTE?")
        t1.clear()
    else:
        continuar = 'nao'

    
                
            
exitonclick()    