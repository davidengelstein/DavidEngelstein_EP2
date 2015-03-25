from turtle import *               # Usa a biblioteca de turtle graphics
window = Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Poligonos")

speed(5)  # define a velocidade
penup()       # Remova e veja o que acontece
setpos(-250,-200)


pendown()
color("orange")


for i in range(1):
    
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
    forward(450)
    left(90)
    forward(50)

  

window.exitonclick()


