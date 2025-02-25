from glob import glob
import os
import turtle
from pathlib import Path

def carrega_personagens():
    cam_personagens = Path(__file__).parent / "personagens"
    cam_atual = Path.cwd()

    os.chdir(cam_personagens.as_posix())
    for img in glob("*.gif"):
        turtle.register_shape(img)

    os.chdir(cam_atual.as_posix())

