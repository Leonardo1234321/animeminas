"""
Módulo principal
"""

import turtle
from pacote import nucleo

# Do módulo menus, do pacote ______, import o menu_principal
from pacote.menus import menu_principal

def cena1():
    """
    Descrição da cena 1
    """
    pass

def cena2():
    """
    Descrição da cena 2
    """    
    pass

def cena3():
    """
    Descrição da cena 3
    """    
    pass

def cena4():
    """
    Descrição da cena 4
    """    
    pass


# Função principal
def main():
    nucleo.carrega_personagens()    
    op = int(input(menu_principal))
    while op != 5:
        if op == 1:
            cena1()
        elif op == 2:
            cena2()
        elif op == 3:
            cena3()
        elif op == 4:
            cena4()
        else:
            print("Opção inválida.")
            
        op = int(input(menu_principal))

# Chamada da função principal
main()