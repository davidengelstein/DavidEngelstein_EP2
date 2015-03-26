#DavidEngelstein
from turtle import *
t1=
window = Screen()    
window.bgcolor("lightblue")
window.title("Jogo da Forca")


speed(5)  
penup()      
setpos(-250,-200)


pendown()
color("black")


def forca():  
    
    left(90)  
    forward(400) 
    right(90)  
    forward(150)
    right(90)  
    forward(50) 
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(250)
    left(90)
    fd(450)
    left(90)
    forward(50)
    penup()
    fd(50)
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
        penup()
        fd(30)
    else:
        pendown()
        fd(30)
        penup()
        fd(7)

def cabeca():
    penup()
    setpos(-75,150)
    pendown()
    left(180)
    circle(40)

def corpo():
    penup()
    setpos(-75,70)
    pendown()
    setpos(-75,-100)
    
def perna1():
    penup()
    setpos(-75,-100)
    pendown()
    left(45)
    fd(100)
    
def perna2():
    penup()
    setpos(-75,-100)
    pendown()
    left(90)
    fd(100)
    
def braco1():
    penup()
    setpos(-75,25)
    pendown()
    fd(100)
    
def braco2():
    penup()
    setpos(-75,25)
    pendown()
    right(90)
    fd(100)

variavel_texto = window.textinput("Nome Janela", "Texto Pergunta")        
  
exitonclick()