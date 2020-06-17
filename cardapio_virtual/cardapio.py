import pygame, pygame.mixer
import os
import sys
from cardapio_virtual.modelo.Usuario import Usuario

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
coca = (50,200,100,100)
guarana = (100,200,100,100)
fantauva = (150,200,100,100)
fantalaranja = (200,200,100,100)
comida1 = (50,50,100,100)
comida2 = (100,50,100,100)
comida3 = (150,50,100,100)
comida4 = (200,50,100,100)

#Som
som = pygame.mixer.Sound('tracks/som.wav')
clique = pygame.mixer.Sound('tracks/clique.wav')
erro = pygame.mixer.Sound('tracks/erro.wav')

#Caixas de Texto
caixaNome = pygame.Rect(240,100,300,100)
caixaCpf = pygame.Rect(240,250,300,100)
caixaEmail = pygame.Rect(240,400,300,100)

#Cores
cor_inativa = pygame.Color('lightskyblue3')
cor_ativa = pygame.Color('dodgerblue2')
corNome = cor_inativa
corCpf = cor_inativa
corEmail = cor_inativa
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
        pygame.draw.rect(screen,corNome,caixaNome,2)
        screen.blit(pygame.font.SysFont("Arial bold",60).render(nome,True,blue),(caixaNome.x+7,caixaNome.y+10))
        screen.blit(pygame.font.SysFont("Arial bold", 30).render(user.getNome(), True, (255, 255, 255)), [250, 120])

        screen.blit(pygame.font.SysFont("Arial bold",30).render("CPF",True,(255,255,255)),[250,220])
        pygame.draw.rect(screen,corCpf,caixaCpf,2)
        screen.blit(pygame.font.SysFont("Arial bold",60).render(cpf,True,blue),(caixaCpf.x+7,caixaCpf.y+10))
        screen.blit(pygame.font.SysFont("Arial bold", 30).render(user.getCpf(), True, (255, 255, 255)), [250, 270])

        screen.blit(pygame.font.SysFont("Arial bold",30).render("E-mail",True,(255,255,255)),[250,370])
        pygame.draw.rect(screen,corEmail,caixaEmail,2)
        screen.blit(pygame.font.SysFont("Arial bold",60).render(email,True,blue),(caixaEmail.x+7,caixaEmail.y+10))
        screen.blit(pygame.font.SysFont("Arial bold", 30).render(user.getEmail(), True, (255, 255, 255)), [250, 420])

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

    elif cena == 3:
        Exibir_Imagem(comida1,'baconOFF.jpg')
        Exibir_Imagem(comida2, 'baconOFF.jpg')
        Exibir_Imagem(comida3, 'baconOFF.jpg')
        Exibir_Imagem(comida4, 'baconOFF.jpg')
        Exibir_Imagem(coca, 'cocaOFF.jpg')
        Exibir_Imagem(guarana, 'guaranaOFF.jpg')
        Exibir_Imagem(fantauva, 'fantauvaOFF.jpg')
        Exibir_Imagem(fantalaranja, 'fantalaranjaOFF.jpg')

    elif cena == 4:
        Exibir_Imagem(coca,'cocaOFF.jpg')
        Exibir_Imagem(guarana,'guaranaOFF.jpg')
        Exibir_Imagem(fantauva,'fantauvaOFF.jpg')
        Exibir_Imagem(fantalaranja,'fantalaranjaOFF.jpg')

    elif cena == 5:
        Exibir_Imagem(coca,'cocaOFF.jpg')
        Exibir_Imagem(guarana,'guaranaOFF.jpg')
        Exibir_Imagem(fantauva,'fantauvaOFF.jpg')
        Exibir_Imagem(fantalaranja,'fantalaranjaOFF.jpg')

    elif cena == 6:
        Exibir_Imagem(coca,'cocaOFF.jpg')
        Exibir_Imagem(guarana,'guaranaOFF.jpg')
        Exibir_Imagem(fantauva,'fantauvaOFF.jpg')
        Exibir_Imagem(fantalaranja,'fantalaranjaOFF.jpg')


def Acoes(cena):
    global nome
    global cpf
    global email
    global nomeAtivo
    global cpfAtivo
    global emailAtivo
    global valido
    global running
    global corNome
    global corCpf
    global corEmail
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if nomeAtivo:
                if event.key == pygame.K_BACKSPACE or len(user.getNome()) > 50:
                    user.backspaceNome()
                elif event.key == 13:
                    nomeAtivo = False
                    corNome = cor_inativa
                    cpfAtivo = True
                    corCpf = cor_ativa
                    return 1
                else:
                    user.appendNome(event.unicode)

            if cpfAtivo:
                if event.key == pygame.K_BACKSPACE or len(user.getCpf()) > 12:
                    user.backspaceCpf()
                elif event.key == 13:
                    cpfAtivo = False
                    corCpf = cor_inativa
                    emailAtivo = True
                    corEmail = cor_ativa
                    return 1
                else:
                    user.appendCpf(event.unicode)

            if emailAtivo:
                if event.key == pygame.K_BACKSPACE or len(user.getEmail()) > 50:
                    user.backspaceEmail()
                else:
                    if event.key != 13:
                        user.appendEmail(event.unicode)
        
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
                    nomeAtivo = True
                    corNome = cor_ativa
                    corCpf = cor_inativa
                    corEmail = cor_inativa
                    
                elif caixaCpf.collidepoint(event.pos):
                    cpfAtivo = True
                    corCpf = cor_ativa
                    corNome = cor_inativa
                    corEmail = cor_inativa
                    
                elif caixaEmail.collidepoint(event.pos):
                    emailAtivo = True
                    corEmail = cor_ativa
                    corNome = cor_inativa
                    corCpf = cor_inativa

                elif pygame.Rect(enviar).collidepoint(event.pos):
                    if len(user.getNome()) > 0 and len(user.getCpf()) == 11 and len(user.getEmail()) > 10:
                        log("Dados de usuário registrados")
                        clique.play()
                        cena = 2
                        return cena
                    else:
                        log("É preciso preencher todos os campos para prosseguir")
                        erro.play()

                else:
                    nomeAtivo = False
                    cpfAtivo = False
                    emailAtivo = False
                    corNome = cor_inativa
                    corCpf = cor_inativa
                    corEmail = cor_inativa

            elif cena == 2:

                if pygame.Rect(r1).collidepoint(event.pos):
                    log("Restaurante 1 selecionado")
                    clique.play()
                    cena = 3
                    return cena

                elif pygame.Rect(r1).collidepoint(event.pos):
                    log("Restaurante 2 selecionado")
                    clique.play()
                    cena = 4
                    return cena

                elif pygame.Rect(r1).collidepoint(event.pos):
                    log("Restaurante 3 selecionado")
                    clique.play()
                    cena = 5
                    return cena

                elif pygame.Rect(r1).collidepoint(event.pos):
                    log("Restaurante 4 selecionado")
                    clique.play()
                    cena = 6
                    return cena

            elif cena == 3:
                break

            elif cena == 4:
                break

            elif cena == 5:
                break

            elif cena == 6:
                break
                
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
