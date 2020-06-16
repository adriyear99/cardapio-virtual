import pygame, pygame.mixer
import os
import sys
from .modelo import Usuario

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)



user = Usuario()


#Variáveis e Flags
nome = ""
cpf = ""
email = ""
nomeAtivo = False
cpfAtivo = False
emailAtivo = False
valido = False

#Imagens
background = (0,0,800,600)
titulo = (130,150,500,100)
cadastrar = (240,270,300,100)
sair = (240,390,300,100)
r1 = (240,100,300,100)
r2 = (240,200,300,100)
r3 = (240,300,300,100)
r4 = (240,400,300,100)
enviar = (240,500,300,100)

#Som
som = pygame.mixer.Sound('tracks/som.wav')
clique = pygame.mixer.Sound('tracks/clique.wav')

#Caixas de Texto
caixaNome = pygame.Rect(240,100,300,100)
caixaCpf = pygame.Rect(240,250,300,100)
caixaEmail = pygame.Rect(240,400,300,100)

#Cores
cor_inativa = pygame.Color('lightskyblue3')
cor_ativa = pygame.Color('dodgerblue2')
cor = cor_inativa
blue = (0,191,255)



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
        Exibir_Imagem(background, 'background_menu.jpg')

        screen.blit(pygame.font.SysFont("Arial bold",30).render("Nome",True,(255,255,255)),[250,70])
        pygame.draw.rect(screen,cor,caixaNome,2)
        screen.blit(pygame.font.SysFont("Arial bold",60).render(nome,True,cor),(caixaNome.x+7,caixaNome.y+10))

        screen.blit(pygame.font.SysFont("Arial bold",30).render("CPF",True,(255,255,255)),[250,220])
        pygame.draw.rect(screen,cor,caixaCpf,2)
        screen.blit(pygame.font.SysFont("Arial bold",60).render(cpf,True,cor),(caixaCpf.x+7,caixaCpf.y+10))

        screen.blit(pygame.font.SysFont("Arial bold",30).render("E-mail",True,(255,255,255)),[250,370])
        pygame.draw.rect(screen,cor,caixaEmail,2)
        screen.blit(pygame.font.SysFont("Arial bold",60).render(email,True,cor),(caixaEmail.x+7,caixaEmail.y+10))

        if not valido:
            Exibir_Imagem(enviar,'enviarOFF.jpg')
        else:
            Exibir_Imagem(enviar, 'enviarON.jpg')

    elif cena == 2:
        Exibir_Imagem(background,'background_menu.jpg')
        Exibir_Imagem(r1,'restaurante1.jpg')
        Exibir_Imagem(r2,'restaurante2.jpg')
        Exibir_Imagem(r3,'restaurante3.jpg')
        Exibir_Imagem(r4,'restaurante4.jpg')


def Acoes(cena):
    global nome
    global cpf
    global email
    global nomeAtivo
    global cpfAtivo
    global emailAtivo
    global valido
    global running
    global cor
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if nomeAtivo:
                if event.key == pygame.K_BACKSPACE or len(user.nome) > 50:
                    user.backspaceNome()
                else:
                    user.nome += event.unicode

            if cpfAtivo:
                if event.key == pygame.K_BACKSPACE or len(user.cpf) > 11:
                    user.backspaceCpf()
                else:
                    user.cpf += event.unicode

            if emailAtivo:
                if event.key == pygame.K_BACKSPACE or len(user.nome) > 50:
                    user.backspaceEmail()
                else:
                    user.email += event.unicode
        
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

                if caixaNome.collidepoint(event.pos):
                    nomeAtivo = not nomeAtivo
                    
                elif caixaCpf.collidepoint(event.pos):
                    cpfAtivo = not cpfAtivo
                    
                elif caixaEmail.collidepoint(event.pos):
                    emailAtivo = not emailAtivo

                elif pygame.Rect(enviar).collidepoint(event.pos):
                    if len(user.nome) > 0 and len(user.cpf) == 11 and len(user.email) > 10:
                        log("Dados de usuário registrados")
                        clique.play()
                        cena = 2
                        return cena
                    
                else:
                    nomeAtivo = False
                    cpfAtivo = False
                    emailAtivo = False
                    

                

            elif cena == 2:

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
