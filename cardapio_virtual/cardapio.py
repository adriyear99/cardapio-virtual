import pygame, pygame.mixer
import os
import sys
from time import sleep
from cardapio_virtual.modelo.Usuario import Usuario

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

#Objeto da classe
user = Usuario()

#Variáveis e Flags
nome = ""
cpf = ""
email = ""
restaurante = 0
anim = 0
nomeAtivo = False
cpfAtivo = False
emailAtivo = False
valido = False
aprovado = False

bacon = False
chicken = False
melt = False
quarterao = False
macarrao = False
pizza = False
pizzaChocolate = False
lasanha = False
carne = False
frango = False
linguica = False
batata = False
sushi = False
sashimi = False
yakisoba = False
rolinho = False
cocaFlag = False
guaranaFlag = False
fantaUvaFlag = False
fantaLaranjaFlag = False

baconMotion = False
chickenMotion = False
meltMotion = False
quarteraoMotion = False
macarraoMotion = False
pizzaMotion = False
pizzaChocolateMotion = False
lasanhaMotion = False
carneMotion = False
frangoMotion = False
linguicaMotion = False
batataMotion = False
sushiMotion = False
sashimiMotion = False
yakisobaMotion = False
rolinhoMotion = False
cocaMotion = False
guaranaMotion = False
fantaUvaMotion = False
fantaLaranjaMotion = False

#Imagens
background = (0,0,800,600)
titulo = (130,150,500,100)
cadastrar = (240,270,300,100)
sair = (240,390,300,100)
r1 = (240,100,300,100)
r2 = (240,200,300,100)
r3 = (240,300,300,100)
r4 = (240,400,300,100)
voltar = (10,10,70,70)
enviar = (260,470,300,100)
confirmar = (200,470,400,100)
mensagem = (80,100,600,150)
comida1 = (80,100,150,150)
comida2 = (230,100,150,150)
comida3 = (380,100,150,150)
comida4 = (530,100,150,150)
coca = (80,270,150,150)
guarana = (230,270,150,150)
fantauva = (380,270,150,150)
fantalaranja = (530,270,150,150)

#Som
som = pygame.mixer.Sound('tracks/som.wav')
clique = pygame.mixer.Sound('tracks/clique.wav')
erro = pygame.mixer.Sound('tracks/erro.wav')

#Caixas de Texto
caixaNome = pygame.Rect(170,70,480,50)
caixaCpf = pygame.Rect(170,220,480,50)
caixaEmail = pygame.Rect(170,370,480,50)

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


def animacao():
    global anim

    bola = (130+50*anim,260,100,100)
    Exibir_Imagem(bola,'bola.png')
    if anim < 9:
        anim += 1
        sleep(1)
    else:
        anim = 0
        sleep(1)


def reset():
    global restaurante
    global bacon
    global chicken
    global melt
    global quarterao
    global macarrao
    global pizza
    global pizzaChocolate
    global lasanha
    global carne
    global frango
    global linguica
    global batata
    global sushi
    global sashimi
    global yakisoba
    global rolinho
    global cocaFlag
    global guaranaFlag
    global fantaUvaFlag
    global fantaLaranjaFlag

    restaurante = 0
    bacon = False
    chicken = False
    melt = False
    quarterao = False
    macarrao = False
    pizza = False
    pizzaChocolate = False
    lasanha = False
    carne = False
    frango = False
    linguica = False
    batata = False
    sushi = False
    sashimi = False
    yakisoba = False
    rolinho = False
    cocaFlag = False
    guaranaFlag = False
    fantaUvaFlag = False
    fantaLaranjaFlag = False


def Exibir(cena):
    global valido
    global aprovado

    if cena == 0:
        Exibir_Imagem(background,'background_menu.jpg')
        Exibir_Imagem(titulo,'titulo.png')
        Exibir_Imagem(cadastrar,'cadastrar.jpg')
        Exibir_Imagem(sair,'sair.jpg')

    elif cena == 1:
        Exibir_Imagem(background,'background_menu.jpg')
        Exibir_Imagem(voltar,'voltar.png')

        screen.blit(pygame.font.SysFont("Arial bold",30).render("Nome",True,(255,255,255)),[180,40])
        pygame.draw.rect(screen,corNome,caixaNome,2)
        screen.blit(pygame.font.SysFont("Arial bold",60).render(nome,True,blue),(caixaNome.x+7,caixaNome.y+10))
        screen.blit(pygame.font.SysFont("Arial bold", 30).render(user.getNome(), True, (255, 255, 255)), [180, 85])

        screen.blit(pygame.font.SysFont("Arial bold",30).render("CPF",True,(255,255,255)),[180,190])
        pygame.draw.rect(screen,corCpf,caixaCpf,2)
        screen.blit(pygame.font.SysFont("Arial bold",60).render(cpf,True,blue),(caixaCpf.x+7,caixaCpf.y+10))
        screen.blit(pygame.font.SysFont("Arial bold", 30).render(user.getCpf(), True, (255, 255, 255)), [180, 235])

        screen.blit(pygame.font.SysFont("Arial bold",30).render("E-mail",True,(255,255,255)),[180,340])
        pygame.draw.rect(screen,corEmail,caixaEmail,2)
        screen.blit(pygame.font.SysFont("Arial bold",60).render(email,True,blue),(caixaEmail.x+7,caixaEmail.y+10))
        screen.blit(pygame.font.SysFont("Arial bold", 30).render(user.getEmail(), True, (255, 255, 255)), [180, 385])

        if len(user.getNome()) > 0 and len(user.getCpf()) == 11 and len(user.getEmail()) > 10:
            Exibir_Imagem(enviar,'enviarON.jpg')
            valido = True
        else:
            Exibir_Imagem(enviar, 'enviarOFF.jpg')
            valido = False

    elif cena == 2:
        Exibir_Imagem(background,'background_menu.jpg')
        Exibir_Imagem(voltar, 'voltar.png')
        Exibir_Imagem(r1,'restaurante1.jpg')
        Exibir_Imagem(r2,'restaurante2.jpg')
        Exibir_Imagem(r3,'restaurante3.jpg')
        Exibir_Imagem(r4,'restaurante4.jpg')

    elif cena == 3:
        Exibir_Imagem(background,'background_menu.jpg')
        Exibir_Imagem(voltar, 'voltar.png')

        if not baconMotion and not bacon:
            Exibir_Imagem(comida1,'baconOFF.jpg')
        else:
            Exibir_Imagem(comida1,'baconON.jpg')

        if not chickenMotion and not chicken:
            Exibir_Imagem(comida2,'chickenOFF.jpg')
        else:
            Exibir_Imagem(comida2,'chickenON.jpg')

        if not meltMotion and not melt:
            Exibir_Imagem(comida3,'meltOFF.jpg')
        else:
            Exibir_Imagem(comida3,'meltON.jpg')

        if not quarteraoMotion and not quarterao:
            Exibir_Imagem(comida4,'quarteraoOFF.jpg')
        else:
            Exibir_Imagem(comida4,'quarteraoON.jpg')

        if not cocaMotion and not cocaFlag:
            Exibir_Imagem(coca,'cocaOFF.jpg')
        else:
            Exibir_Imagem(coca,'cocaON.jpg')

        if not guaranaMotion and not guaranaFlag:
            Exibir_Imagem(guarana, 'guaranaOFF.jpg')
        else:
            Exibir_Imagem(guarana,'guaranaON.jpg')

        if not fantaUvaMotion and not fantaUvaFlag:
            Exibir_Imagem(fantauva, 'fantauvaOFF.jpg')
        else:
            Exibir_Imagem(fantauva, 'fantauvaON.jpg')

        if not fantaLaranjaMotion and not fantaLaranjaFlag:
            Exibir_Imagem(fantalaranja, 'fantalaranjaOFF.jpg')
        else:
            Exibir_Imagem(fantalaranja,'fantalaranjaON.jpg')

        if bacon or chicken or melt or quarterao or cocaFlag or guaranaFlag or fantaUvaFlag or fantaLaranjaFlag:
            Exibir_Imagem(enviar,'enviarON.jpg')
            aprovado = True
        else:
            Exibir_Imagem(enviar, 'enviarOFF.jpg')
            aprovado = False

    elif cena == 4:
        Exibir_Imagem(background,'background_menu.jpg')
        Exibir_Imagem(voltar, 'voltar.png')

        if not macarraoMotion and not macarrao:
            Exibir_Imagem(comida1,'macarraoOFF.jpg')
        else:
            Exibir_Imagem(comida1,'macarraoON.jpg')

        if not pizzaMotion and not pizza:
            Exibir_Imagem(comida2,'pizzaOFF.jpg')
        else:
            Exibir_Imagem(comida2,'pizzaON.jpg')

        if not pizzaChocolateMotion and not pizzaChocolate:
            Exibir_Imagem(comida3,'pizzachocolateOFF.jpg')
        else:
            Exibir_Imagem(comida3,'pizzachocolateON.jpg')

        if not lasanhaMotion and not lasanha:
            Exibir_Imagem(comida4,'lasanhaOFF.jpg')
        else:
            Exibir_Imagem(comida4,'lasanhaON.jpg')

        if not cocaMotion and not cocaFlag:
            Exibir_Imagem(coca,'cocaOFF.jpg')
        else:
            Exibir_Imagem(coca,'cocaON.jpg')

        if not guaranaMotion and not guaranaFlag:
            Exibir_Imagem(guarana, 'guaranaOFF.jpg')
        else:
            Exibir_Imagem(guarana,'guaranaON.jpg')

        if not fantaUvaMotion and not fantaUvaFlag:
            Exibir_Imagem(fantauva, 'fantauvaOFF.jpg')
        else:
            Exibir_Imagem(fantauva, 'fantauvaON.jpg')

        if not fantaLaranjaMotion and not fantaLaranjaFlag:
            Exibir_Imagem(fantalaranja, 'fantalaranjaOFF.jpg')
        else:
            Exibir_Imagem(fantalaranja,'fantalaranjaON.jpg')

        if macarrao or pizza or pizzaChocolate or lasanha or cocaFlag or guaranaFlag or fantaUvaFlag or fantaLaranjaFlag:
            Exibir_Imagem(enviar,'enviarON.jpg')
            aprovado = True
        else:
            Exibir_Imagem(enviar, 'enviarOFF.jpg')
            aprovado = False

    elif cena == 5:
        Exibir_Imagem(background,'background_menu.jpg')
        Exibir_Imagem(voltar, 'voltar.png')

        if not carneMotion and not carne:
            Exibir_Imagem(comida1,'carneOFF.jpg')
        else:
            Exibir_Imagem(comida1,'carneON.jpg')

        if not frangoMotion and not frango:
            Exibir_Imagem(comida2,'frangoOFF.jpg')
        else:
            Exibir_Imagem(comida2,'frangoON.jpg')

        if not linguicaMotion and not linguica:
            Exibir_Imagem(comida3,'linguiçaOFF.jpg')
        else:
            Exibir_Imagem(comida3,'linguiçaON.jpg')

        if not batataMotion and not batata:
            Exibir_Imagem(comida4,'batataOFF.jpg')
        else:
            Exibir_Imagem(comida4,'batataON.jpg')

        if not cocaMotion and not cocaFlag:
            Exibir_Imagem(coca,'cocaOFF.jpg')
        else:
            Exibir_Imagem(coca,'cocaON.jpg')

        if not guaranaMotion and not guaranaFlag:
            Exibir_Imagem(guarana, 'guaranaOFF.jpg')
        else:
            Exibir_Imagem(guarana,'guaranaON.jpg')

        if not fantaUvaMotion and not fantaUvaFlag:
            Exibir_Imagem(fantauva, 'fantauvaOFF.jpg')
        else:
            Exibir_Imagem(fantauva, 'fantauvaON.jpg')

        if not fantaLaranjaMotion and not fantaLaranjaFlag:
            Exibir_Imagem(fantalaranja, 'fantalaranjaOFF.jpg')
        else:
            Exibir_Imagem(fantalaranja,'fantalaranjaON.jpg')

        if carne or frango or linguica or batata or cocaFlag or guaranaFlag or fantaUvaFlag or fantaLaranjaFlag:
            Exibir_Imagem(enviar,'enviarON.jpg')
            aprovado = True
        else:
            Exibir_Imagem(enviar, 'enviarOFF.jpg')
            aprovado = False

    elif cena == 6:
        Exibir_Imagem(background,'background_menu.jpg')
        Exibir_Imagem(voltar, 'voltar.png')

        if not sushiMotion and not sushi:
            Exibir_Imagem(comida1,'sushiOFF.jpg')
        else:
            Exibir_Imagem(comida1,'sushiON.jpg')

        if not sashimiMotion and not sashimi:
            Exibir_Imagem(comida2,'sashimiOFF.jpg')
        else:
            Exibir_Imagem(comida2,'sashimiON.jpg')

        if not yakisobaMotion and not yakisoba:
            Exibir_Imagem(comida3,'yakisobaOFF.jpg')
        else:
            Exibir_Imagem(comida3,'yakisobaON.jpg')

        if not rolinhoMotion and not rolinho:
            Exibir_Imagem(comida4,'rolinhoOFF.jpg')
        else:
            Exibir_Imagem(comida4,'rolinhoON.jpg')

        if not cocaMotion and not cocaFlag:
            Exibir_Imagem(coca,'cocaOFF.jpg')
        else:
            Exibir_Imagem(coca,'cocaON.jpg')

        if not guaranaMotion and not guaranaFlag:
            Exibir_Imagem(guarana, 'guaranaOFF.jpg')
        else:
            Exibir_Imagem(guarana,'guaranaON.jpg')

        if not fantaUvaMotion and not fantaUvaFlag:
            Exibir_Imagem(fantauva, 'fantauvaOFF.jpg')
        else:
            Exibir_Imagem(fantauva, 'fantauvaON.jpg')

        if not fantaLaranjaMotion and not fantaLaranjaFlag:
            Exibir_Imagem(fantalaranja, 'fantalaranjaOFF.jpg')
        else:
            Exibir_Imagem(fantalaranja,'fantalaranjaON.jpg')

        if sushi or sashimi or yakisoba or rolinho or cocaFlag or guaranaFlag or fantaUvaFlag or fantaLaranjaFlag:
            Exibir_Imagem(enviar,'enviarON.jpg')
            aprovado = True
        else:
            Exibir_Imagem(enviar, 'enviarOFF.jpg')
            aprovado = False

    elif cena == 7:
        Exibir_Imagem(background,'background_menu.jpg')
        Exibir_Imagem(voltar,'voltar.png')
        Exibir_Imagem(confirmar,'confirmar.jpg')

        if cocaFlag:
            Exibir_Imagem(coca,'cocaON.jpg')
        if guaranaFlag:
            Exibir_Imagem(guarana,'guaranaON.jpg')
        if fantaUvaFlag:
            Exibir_Imagem(fantauva,'fantauvaON.jpg')
        if fantaLaranjaFlag:
            Exibir_Imagem(fantalaranja,'fantalaranjaON.jpg')

        if restaurante == 1:
            if bacon:
                Exibir_Imagem(comida1,'baconON.jpg')
            if chicken:
                Exibir_Imagem(comida2,'chickenON.jpg')
            if melt:
                Exibir_Imagem(comida3,'meltON.jpg')
            if quarterao:
                Exibir_Imagem(comida4,'quarteraoON.jpg')
        elif restaurante == 2:
            if macarrao:
                Exibir_Imagem(comida1,'macarraoON.jpg')
            if pizza:
                Exibir_Imagem(comida2,'pizzaON.jpg')
            if pizzaChocolate:
                Exibir_Imagem(comida3,'pizzachocolateON.jpg')
            if lasanha:
                Exibir_Imagem(comida4,'lasanhaON.jpg')
        elif restaurante == 3:
            if carne:
                Exibir_Imagem(comida1,'carneON.jpg')
            if frango:
                Exibir_Imagem(comida2,'frangoON.jpg')
            if linguica:
                Exibir_Imagem(comida3,'linguiçaON.jpg')
            if batata:
                Exibir_Imagem(comida4,'batataON.jpg')
        elif restaurante == 4:
            if sushi:
                Exibir_Imagem(comida1,'sushiON.jpg')
            if sashimi:
                Exibir_Imagem(comida2,'sashimiON.jpg')
            if yakisoba:
                Exibir_Imagem(comida3,'yakisobaON.jpg')
            if rolinho:
                Exibir_Imagem(comida4,'rolinhoON.jpg')

    elif cena == 8:
        Exibir_Imagem(background,'background_menu.jpg')
        Exibir_Imagem(mensagem,'mensagem.png')
        animacao()
        Exibir_Imagem(sair,'sair.jpg')


def Acoes(cena):
    global nome
    global cpf
    global email
    global restaurante
    global nomeAtivo
    global cpfAtivo
    global emailAtivo
    global valido
    global running
    global corNome
    global corCpf
    global corEmail

    global bacon
    global chicken
    global melt
    global quarterao
    global macarrao
    global pizza
    global pizzaChocolate
    global lasanha
    global carne
    global frango
    global linguica
    global batata
    global sushi
    global sashimi
    global yakisoba
    global rolinho
    global cocaFlag
    global guaranaFlag
    global fantaUvaFlag
    global fantaLaranjaFlag

    global baconMotion
    global chickenMotion
    global meltMotion
    global quarteraoMotion
    global macarraoMotion
    global pizzaMotion
    global pizzaChocolateMotion
    global lasanhaMotion
    global carneMotion
    global frangoMotion
    global linguicaMotion
    global batataMotion
    global sushiMotion
    global sashimiMotion
    global yakisobaMotion
    global rolinhoMotion
    global cocaMotion
    global guaranaMotion
    global fantaUvaMotion
    global fantaLaranjaMotion
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEMOTION:

            if pygame.Rect(coca).collidepoint(event.pos):
                cocaMotion = True
            else:
                cocaMotion = False

            if pygame.Rect(guarana).collidepoint(event.pos):
                guaranaMotion = True
            else:
                guaranaMotion = False

            if pygame.Rect(fantauva).collidepoint(event.pos):
                fantaUvaMotion = True
            else:
                fantaUvaMotion = False

            if pygame.Rect(fantalaranja).collidepoint(event.pos):
                fantaLaranjaMotion = True
            else:
                fantaLaranjaMotion = False

            if cena == 3:
                if pygame.Rect(comida1).collidepoint(event.pos):
                    baconMotion = True
                else:
                    baconMotion = False

                if pygame.Rect(comida2).collidepoint(event.pos):
                    chickenMotion = True
                else:
                    chickenMotion = False

                if pygame.Rect(comida3).collidepoint(event.pos):
                    meltMotion = True
                else:
                    meltMotion = False

                if pygame.Rect(comida4).collidepoint(event.pos):
                    quarteraoMotion = True
                else:
                    quarteraoMotion = False

            elif cena == 4:
                if pygame.Rect(comida1).collidepoint(event.pos):
                    macarraoMotion = True
                else:
                    macarraoMotion = False

                if pygame.Rect(comida2).collidepoint(event.pos):
                    pizzaMotion = True
                else:
                    pizzaMotion = False

                if pygame.Rect(comida3).collidepoint(event.pos):
                    pizzaChocolateMotion = True
                else:
                    pizzaChocolateMotion = False

                if pygame.Rect(comida4).collidepoint(event.pos):
                    lasanhaMotion = True
                else:
                    lasanhaMotion = False

            elif cena == 5:
                if pygame.Rect(comida1).collidepoint(event.pos):
                    carneMotion = True
                else:
                    carneMotion = False

                if pygame.Rect(comida2).collidepoint(event.pos):
                    frangoMotion = True
                else:
                    frangoMotion = False

                if pygame.Rect(comida3).collidepoint(event.pos):
                    linguicaMotion = True
                else:
                    linguicaMotion = False

                if pygame.Rect(comida4).collidepoint(event.pos):
                    batataMotion = True
                else:
                    batataMotion = False

            elif cena == 6:
                if pygame.Rect(comida1).collidepoint(event.pos):
                    sushiMotion = True
                else:
                    sushiMotion = False

                if pygame.Rect(comida2).collidepoint(event.pos):
                    sashimiMotion = True
                else:
                    sashimiMotion = False

                if pygame.Rect(comida3).collidepoint(event.pos):
                    yakisobaMotion = True
                else:
                    yakisobaMotion = False

                if pygame.Rect(comida4).collidepoint(event.pos):
                    rolinhoMotion = True
                else:
                    rolinhoMotion = False


        elif event.type == pygame.KEYDOWN:
            if nomeAtivo:
                if event.key == pygame.K_BACKSPACE or len(user.getNome()) > 40:
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
                if event.key == pygame.K_BACKSPACE or len(user.getCpf()) > 11:
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
                if event.key == pygame.K_BACKSPACE or len(user.getEmail()) > 40:
                    user.backspaceEmail()
                else:
                    if event.key != 13:
                        user.appendEmail(event.unicode)
                    else:
                        if len(user.getNome()) > 0 and len(user.getCpf()) == 11 and len(user.getEmail()) > 10:
                            log("Indo para a tela de escolha de restaurante")
                            cena += 1
                            return cena
                        else:
                            erro.play()
                            log("Preencha todos os dados corretamente antes de prosseguir")
        
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if cena == 0:

                if pygame.Rect(cadastrar).collidepoint(event.pos):
                    log("Indo para a tela de cadastro")
                    clique.play()
                    cena += 1
                    return cena

                elif pygame.Rect(sair).collidepoint(event.pos):
                    log("Saindo do aplicativo")
                    clique.play()
                    pygame.quit()
                    sys.exit()

            elif cena == 1:

                if pygame.Rect(voltar).collidepoint(event.pos):
                    log("Voltando para a tela inicial")
                    cena -= 1
                    return cena

                if caixaNome.collidepoint(event.pos):
                    nomeAtivo = True
                    cpfAtivo = False
                    emailAtivo = False
                    corNome = cor_ativa
                    corCpf = cor_inativa
                    corEmail = cor_inativa
                    
                elif caixaCpf.collidepoint(event.pos):
                    cpfAtivo = True
                    nomeAtivo = False
                    emailAtivo = False
                    corCpf = cor_ativa
                    corNome = cor_inativa
                    corEmail = cor_inativa
                    
                elif caixaEmail.collidepoint(event.pos):
                    emailAtivo = True
                    nomeAtivo = False
                    cpfAtivo = False
                    corEmail = cor_ativa
                    corNome = cor_inativa
                    corCpf = cor_inativa

                elif pygame.Rect(enviar).collidepoint(event.pos):
                    if valido:
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

                if pygame.Rect(voltar).collidepoint(event.pos):
                    log("Voltando para a tela de cadastro")
                    cena -= 1
                    return cena

                elif pygame.Rect(r1).collidepoint(event.pos):
                    log("Restaurante 1 selecionado")
                    clique.play()
                    cena += 1
                    return cena

                elif pygame.Rect(r2).collidepoint(event.pos):
                    log("Restaurante 2 selecionado")
                    clique.play()
                    cena += 2
                    return cena

                elif pygame.Rect(r3).collidepoint(event.pos):
                    log("Restaurante 3 selecionado")
                    clique.play()
                    cena += 3
                    return cena

                elif pygame.Rect(r4).collidepoint(event.pos):
                    log("Restaurante 4 selecionado")
                    clique.play()
                    cena += 4
                    return cena

            elif cena == 3:
                if pygame.Rect(voltar).collidepoint(event.pos):
                    log("Voltando para a tela de restaurantes")
                    reset()
                    cena -= 1
                    return cena

                elif pygame.Rect(comida1).collidepoint(event.pos):
                    if not bacon:
                        log("Sanduíche 1 selecionado")
                        clique.play()
                        bacon = True
                    else:
                        clique.play()
                        bacon = False

                elif pygame.Rect(comida2).collidepoint(event.pos):
                    if not chicken:
                        log("Sanduíche 2 selecionado")
                        clique.play()
                        chicken = True
                    else:
                        clique.play()
                        chicken = False

                elif pygame.Rect(comida3).collidepoint(event.pos):
                    if not melt:
                        log("Sanduíche 3 selecionado")
                        clique.play()
                        melt = True
                    else:
                        clique.play()
                        melt = False

                elif pygame.Rect(comida4).collidepoint(event.pos):
                    if not quarterao:
                        log("Sanduíche 4 selecionado")
                        clique.play()
                        quarterao = True
                    else:
                        clique.play()
                        quarterao = False

                elif pygame.Rect(enviar).collidepoint(event.pos):
                    if aprovado:
                        log("Pedido aprovado")
                        clique.play()
                        restaurante = 1
                        cena += 4
                        return cena
                    else:
                        log("Carrinho vazio")
                        erro.play()

            elif cena == 4:
                if pygame.Rect(voltar).collidepoint(event.pos):
                    log("Voltando para a tela de restaurantes")
                    reset()
                    cena -= 2
                    return cena
                elif pygame.Rect(comida1).collidepoint(event.pos):
                    if not macarrao:
                        log("Macarrão selecionado")
                        clique.play()
                        macarrao = True
                    else:
                        clique.play()
                        macarrao = False

                elif pygame.Rect(comida2).collidepoint(event.pos):
                    if not pizza:
                        log("Pizza selecionada")
                        clique.play()
                        pizza = True
                    else:
                        clique.play()
                        pizza = False

                elif pygame.Rect(comida3).collidepoint(event.pos):
                    if not pizzaChocolate:
                        log("Pizza de chocolate selecionada")
                        clique.play()
                        pizzaChocolate = True
                    else:
                        clique.play()
                        pizzaChocolate = False

                elif pygame.Rect(comida4).collidepoint(event.pos):
                    if not lasanha:
                        log("Lasanha selecionada")
                        clique.play()
                        lasanha = True
                    else:
                        clique.play()
                        lasanha = False

                elif pygame.Rect(enviar).collidepoint(event.pos):
                    if aprovado:
                        log("Pedido aprovado")
                        clique.play()
                        restaurante = 2
                        cena += 3
                        return cena
                    else:
                        log("Carrinho vazio")
                        erro.play()

            elif cena == 5:
                if pygame.Rect(voltar).collidepoint(event.pos):
                    log("Voltando para a tela de restaurantes")
                    reset()
                    cena -= 3
                    return cena

                elif pygame.Rect(comida1).collidepoint(event.pos):
                    if not carne:
                        log("Carne selecionada")
                        clique.play()
                        carne = True
                    else:
                        clique.play()
                        carne = False

                elif pygame.Rect(comida2).collidepoint(event.pos):
                    if not frango:
                        log("Frango selecionado")
                        clique.play()
                        frango = True
                    else:
                        clique.play()
                        frango = False

                elif pygame.Rect(comida3).collidepoint(event.pos):
                    if not linguica:
                        log("Linguiça selecionada")
                        clique.play()
                        linguica = True
                    else:
                        clique.play()
                        linguica = False

                elif pygame.Rect(comida4).collidepoint(event.pos):
                    if not batata:
                        log("Batata selecionada")
                        clique.play()
                        batata = True
                    else:
                        clique.play()
                        batata = False

                elif pygame.Rect(enviar).collidepoint(event.pos):
                    if aprovado:
                        log("Pedido aprovado")
                        clique.play()
                        restaurante = 3
                        cena += 2
                        return cena
                    else:
                        log("Carrinho vazio")
                        erro.play()

            elif cena == 6:
                if pygame.Rect(voltar).collidepoint(event.pos):
                    log("Voltando para a tela de restaurantes")
                    reset()
                    cena -= 4
                    return cena

                elif pygame.Rect(comida1).collidepoint(event.pos):
                    if not sushi:
                        log("Sushi selecionado")
                        clique.play()
                        sushi = True
                    else:
                        clique.play()
                        sushi = False

                elif pygame.Rect(comida2).collidepoint(event.pos):
                    if not sashimi:
                        log("Sashimi selecionado")
                        clique.play()
                        sashimi = True
                    else:
                        clique.play()
                        sashimi = False

                elif pygame.Rect(comida3).collidepoint(event.pos):
                    if not yakisoba:
                        log("Yakisoba selecionado")
                        clique.play()
                        yakisoba = True
                    else:
                        clique.play()
                        yakisoba = False

                elif pygame.Rect(comida4).collidepoint(event.pos):
                    if not rolinho:
                        log("Rolinho selecionado")
                        clique.play()
                        rolinho = True
                    else:
                        clique.play()
                        rolinho = False

                elif pygame.Rect(enviar).collidepoint(event.pos):
                    if aprovado:
                        log("Pedido aprovado")
                        clique.play()
                        restaurante = 4
                        cena += 1
                        return cena
                    else:
                        log("Carrinho vazio")
                        erro.play()

            elif cena == 7:
                if pygame.Rect(voltar).collidepoint(event.pos):
                    log("Voltando para a tela de restaurantes")
                    clique.play()
                    reset()
                    cena -= 5
                    return cena

                elif pygame.Rect(confirmar).collidepoint(event.pos):
                    log("Pedido confirmado")
                    clique.play()
                    cena += 1
                    return cena

            elif cena == 8:
                if pygame.Rect(sair).collidepoint(event.pos):
                    log("Saindo do aplicativo")
                    clique.play()
                    running = False
                    pygame.quit()
                    sys.exit()


            if 2 < cena < 7:
                if pygame.Rect(coca).collidepoint(event.pos):
                    if not cocaFlag:
                        log("Coca-Cola selecionada")
                        clique.play()
                        cocaFlag = True
                    else:
                        clique.play()
                        cocaFlag = False

                elif pygame.Rect(guarana).collidepoint(event.pos):
                    if not guaranaFlag:
                        log("Guaraná selecionado")
                        clique.play()
                        guaranaFlag = True
                    else:
                        clique.play()
                        guaranaFlag = False

                elif pygame.Rect(fantauva).collidepoint(event.pos):
                    if not fantaUvaFlag:
                        log("Fanta Uva selecionada")
                        clique.play()
                        fantaUvaFlag = True
                    else:
                        clique.play()
                        fantaUvaFlag = False

                elif pygame.Rect(fantalaranja).collidepoint(event.pos):
                    if not fantaLaranjaFlag:
                        log("Fanta Laranja selecionada")
                        clique.play()
                        fantaLaranjaFlag = True
                    else:
                        clique.play()
                        fantaLaranjaFlag = False
                
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
