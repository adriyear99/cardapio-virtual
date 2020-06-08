import pygame,pygame.mixer
import os
import sys

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)



class usuario:
    pass



#Imagens
background = (0,0,800,600)
titulo = (130,150,500,100)
cadastrar = (240,270,300,100)
sair = (240,390,300,100)
r1 = (240,100,300,100)
r2 = (240,200,300,100)
r3 = (240,300,300,100)
r4 = (240,400,300,100)

#Som
som = pygame.mixer.Sound('tracks/som.wav')
clique = pygame.mixer.Sound('tracks/clique.wav')





def Exibir_Imagem(dados,nome):
    pos_x,pos_y,largura,altura = dados
    image = pygame.image.load(os.path.join("images",nome))
    image = pygame.transform.scale(image,(largura,altura))
    screen.blit(image,(pos_x,pos_y))


def log(texto):
    print(f"REGISTRO: {texto}")


def Exibir(cena):
    
    if cena == 0:
        Exibir_Imagem(background,'background_menu.jpg')
        Exibir_Imagem(titulo,'titulo.jpg')
        Exibir_Imagem(cadastrar,'cadastrar.jpg')
        Exibir_Imagem(sair,'sair.jpg')

    elif cena == 1:
        Exibir_Imagem(background,'background_menu.jpg')
        Exibir_Imagem(r1,'restaurante1.jpg')
        Exibir_Imagem(r2,'restaurante2.jpg')
        Exibir_Imagem(r3,'restaurante3.jpg')
        Exibir_Imagem(r4,'restaurante4.jpg')


def Acoes(cena):
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if cena == 0:

                if pygame.Rect(cadastrar).collidepoint(event.pos):
                    log("Indo para tela de cadastro")
                    clique.play()
                    cena = 1
                    return cena

                elif pygame.Rect(sair).collidepoint(event.pos):
                    log("Saindo do aplicativo")
                    clique.play()
                    pygame.quit()
                    sys.exit()

            elif cena == 1:

                if pygame.Rect(r1).collidepoint(event.pos):
                    log("Restaurante 1 selecionado")
                    clique.play()
                    cena = 2
                    return cena

                elif pygame.Rect(r1).collidepoint(event.pos):
                    log("Restaurante 2 selecionado")
                    clique.play()
                    cena = 3
                    return cena

                elif pygame.Rect(r1).collidepoint(event.pos):
                    log("Restaurante 3 selecionado")
                    clique.play()
                    cena = 4
                    return cena

                elif pygame.Rect(r1).collidepoint(event.pos):
                    log("Restaurante 4 selecionado")
                    clique.play()
                    cena = 5
                    return cena

                
    return cena

                





screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Cardápio Virtual")
running = True
flag_cena_song = True
cena = 0
som.play(loops = -1)

log("Iniciando Aplicativo.")
log("Iniciando Aplicativo..")
log("Iniciando Aplicativo...")

while running:
    if flag_cena_song == False:
        pygame.mixer.pause()
    else:
        pygame.mixer.unpause()

    Exibir(cena)
    cena = Acoes(cena)
    pygame.display.update()
    pygame.display.flip()
