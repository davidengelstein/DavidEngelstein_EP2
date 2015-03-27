#DavidEngelstein
from turtle import *
t1 = Turtle()
window = Screen() 
window.bgcolor("lightblue")
window.title("Jogo da Forca")


t1.speed(5)  
t1.penup()      
t1.setpos(-250,-200)


t1.pendown()
t1.color("black")


def forca():  
    
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
forca()
  
palavras=open("entrada.txt", encoding="utf-8")
leitura=palavras.readlines()
lista=[]
for i in leitura:
    linha=i.strip()
    if linha!="":
        lista.append(linha)
from random import choice
sorteio = choice(lista)
print(sorteio)

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

erro = 0 
while erro<=6:    
     
    variavel = window.textinput("Nome Janela", "Texto Pergunta")    
    for i in range(len(sorteio)):
        
        if variavel == sorteio[i]:
            t1.setpos(-200+i*40,-200)
            pendown()
            t1.write (variavel)
            penup()
    if variavel not in sorteio:
            erro=erro+1
            print(erro)
                    
            if erro == 1:
                cabeca()
            if erro == 2:
                corpo()
            if erro == 3:
                perna1()
            if erro == 4:
                perna2()
            if erro == 5:
                braco1()
            if erro == 6:
                braco2()
                print('vc perdeu')
                break    
                
            
            
         
exitonclick()    