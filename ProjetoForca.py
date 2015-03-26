#DavidEngelstein
from turtle import *
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
  