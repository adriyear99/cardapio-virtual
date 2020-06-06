from venv import *
import os
import platform
import locale


menu = True
while menu:
    print("""
    1.Cadastrar usuario
    2.Consultar menu
    3.Realizar pedido
    4.Selecionar restaurante
    """)
    menu = input("Escolha uma opção? ")
    if menu == "1":
        exec(open('database.py').read())
        exec(open('main.py').read())
    elif menu == "2":
        exec(open('menu.py').read())
    elif menu == "3":
       exec(open('pedido.py').read())
    elif menu == "4":
        exec(open('mi.py').read())
    elif menu != "":
        print("\n Opção Invalida. Tente Novamente")