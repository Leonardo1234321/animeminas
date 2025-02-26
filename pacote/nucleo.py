from glob import glob
import os
import turtle
from pathlib import Path

# Configurações do balão
global balao
balao = turtle.Turtle()
balao.hideturtle()
balao.down()

def carrega_personagens():
    cam_personagens = Path(__file__).parent / "personagens"
    cam_atual = Path.cwd()

    os.chdir(cam_personagens.as_posix())
    for img in glob("*.gif"):
        turtle.register_shape(img)

    os.chdir(cam_atual.as_posix())

def fala(personagem: turtle.Turtle, 
         texto: str, 
         angulo: int, 
         distancia: int,
         tempo: float):
    
    x,y = personagem.pos()
    balao.goto(x, y)   
    balao.left(angulo)
    balao.forward(distancia)
    balao.write(fala)
    sleep(tempo)
    balao.undo()
    balao.undo()
    balao.undo()

