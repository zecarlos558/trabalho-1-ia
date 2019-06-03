import pygame
import sys
import MissionariosCanibais1

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
amarelo = (255,255,0)
laranja = (255,165,0)
rosa = (255,192,203)

try:
    print(pygame.init())
except:
    print("O pygame não foi inicializado corretamente!")
j = 230
altura = 700
largura = 1280
tamanho = 100
pos_x = largura/2
pos_y = altura/2
velocidade_x = 0
velocidade_y = 0
posx = 230
posy = 540
#velocidade_x = 5
#posx = posx + velocidade_x

#Margem Esquerda
#fundo.fill(branco)
#fundo.blit(imagem_rio, (0, 0))
#fundo.blit(imagem_missionario1,(1,400))
#fundo.blit(imagem_missionario2,(60,400))
#fundo.blit(imagem_missionario3,(120,400))
#fundo.blit(imagem_canibal1,(190,400))
#fundo.blit(imagem_canibal2,(260,400))
#fundo.blit(imagem_canibal3,(330,400))                 
#fundo.blit(imagem_barco,(posx,posy))
#Em cima do barco - fundo.blit(imagem_missionario1,(260,500))
#Em cima do barco - fundo.blit(imagem_canibal1,(340,500))

#Margem Direita
#fundo.fill(branco)
#fundo.blit(imagem_rio, (0, 0))
#fundo.blit(imagem_missionario1,(930,400))
#fundo.blit(imagem_missionario2,(865,400))
#fundo.blit(imagem_missionario3,(800,400))
#fundo.blit(imagem_canibal1,(995,400))
#fundo.blit(imagem_canibal2,(1070,400))
#fundo.blit(imagem_canibal3,(1145,400))                 
#fundo.blit(imagem_barco,(800,posy))
#Em cima do barco - fundo.blit(imagem_missionario1,(860,500))
#Em cima do barco - fundo.blit(imagem_canibal1,(940,500))


def deslocarCanoa (resultado,i):
    velocidade = 4
    j = 230
    if (resultado[i][0] == 3 and resultado[i][1] == 3):
        fundo.fill(branco)
        fundo.blit(imagem_rio, (0, 0))
        fundo.blit(imagem_missionario1,(1,400))
        fundo.blit(imagem_missionario2,(60,400))
        fundo.blit(imagem_missionario3,(120,400))
        fundo.blit(imagem_canibal1,(190,400))
        fundo.blit(imagem_canibal2,(260,400))
        fundo.blit(imagem_canibal3,(330,400))
        fundo.blit(imagem_barco,(posx,posy))
        return

    if (resultado[i][2] == 3 and resultado[i][3] == 3):
        fundo.fill(branco)
        fundo.blit(imagem_rio, (0, 0))
        fundo.blit(imagem_missionario1,(930,400))
        fundo.blit(imagem_missionario2,(865,400))
        fundo.blit(imagem_missionario3,(800,400))
        fundo.blit(imagem_canibal1,(995,400))
        fundo.blit(imagem_canibal2,(1070,400))
        fundo.blit(imagem_canibal3,(1145,400))                 
        fundo.blit(imagem_barco,(800,posy))
        return

    if resultado[i][-1] == 0:
        if (resultado[i][2] < resultado[i-1][2] and resultado[i][3] < resultado[i-1][3]):
            fundo.blit(imagem_barco,(800-velocidade,posy))
            fundo.blit(imagem_missionario1,(860-velocidade,500))
            fundo.blit(imagem_canibal1,(940-velocidade,500))
            return
        if (resultado[i][2] < resultado[i-1][2]):
            fundo.blit(imagem_barco,(800-velocidade,posy))
            fundo.blit(imagem_missionario1,(860-velocidade,500))
            return
        if (resultado[i][3] < resultado[i-1][3]):
            fundo.blit(imagem_barco,(800-velocidade,posy))
            fundo.blit(imagem_canibal1,(940-velocidade,500))
            return
    else:
        if (resultado[i][0] < resultado[i-1][0] and resultado[i][1] < resultado[i-1][1]):
            fundo.blit(imagem_barco,(posx+velocidade,posy))
            fundo.blit(imagem_missionario1,(260+velocidade,500))
            fundo.blit(imagem_canibal1,(340+velocidade,500))
            pygame.display.update( )
            return
        if (resultado[i][0] < resultado[i-1][0]):
            fundo.blit(imagem_barco,(posx+velocidade,posy))
            fundo.blit(imagem_missionario1,(260+velocidade,500))
            return
        if (resultado[i][1] < resultado[i-1][1]):
            fundo.blit(imagem_barco,(posx+velocidade,posy))
            fundo.blit(imagem_canibal1,(340+velocidade,500))
            return
    return
velocidade = 5
def desloc1():
    fundo.fill(branco)
    fundo.blit(imagem_rio, (0, 0))
    fundo.blit(imagem_missionario1,(1,400))
    fundo.blit(imagem_missionario2,(60,400))
    fundo.blit(imagem_missionario3,(120,400))
    fundo.blit(imagem_canibal1,(190,400))
    fundo.blit(imagem_canibal2,(260,400))
    fundo.blit(imagem_canibal3,(330,400))
    fundo.blit(imagem_barco,(posx,posy))
    return

def desloc2():
    desloc1()
    posx_b = 230
    posx_m = 260
    posx_c = 340
    def carregarFundo():
        fundo.fill(branco)
        fundo.blit(imagem_rio, (0, 0))
        fundo.blit(imagem_missionario1,(1,400))
        fundo.blit(imagem_missionario2,(60,400))
        fundo.blit(imagem_canibal1,(190,400))
        fundo.blit(imagem_canibal2,(260,400))
    carregarFundo()
    while posx_b < 800:
        fundo.blit(imagem_barco,(posx_b,posy))
        fundo.blit(imagem_missionario3,(posx_m,500))
        fundo.blit(imagem_canibal3,(posx_c,500))
        posx_b = posx_b + velocidade
        posx_m = posx_m + velocidade
        posx_c = posx_c + velocidade
        pygame.display.update( )
        carregarFundo()


def desloc3():
    desloc2()

    posx_b = 800
    posx_m = 860
    def carregarFundo():
        fundo.fill(branco)
        fundo.blit(imagem_rio, (0, 0))
        fundo.blit(imagem_missionario1,(1,400))
        fundo.blit(imagem_missionario2,(60,400))
        fundo.blit(imagem_canibal1,(190,400))
        fundo.blit(imagem_canibal2,(260,400))
        fundo.blit(imagem_canibal3,(1145,400))
    carregarFundo()
    while posx_b > 230:
        fundo.blit(imagem_barco,(posx_b,posy))
        fundo.blit(imagem_missionario3,(posx_m,500))
        posx_b = posx_b - velocidade
        posx_m = posx_m - velocidade
        pygame.display.update( )
        carregarFundo()

def desloc4():
    desloc3()
    posx_b = 230
    posx_c1 = 260
    posx_c2 = 340
    def carregarFundo():
        fundo.fill(branco)
        fundo.blit(imagem_rio, (0, 0))
        fundo.blit(imagem_missionario1,(1,400))
        fundo.blit(imagem_missionario2,(60,400))
        fundo.blit(imagem_missionario3,(120,400))
        fundo.blit(imagem_canibal3,(1145,400))
    carregarFundo()
    while posx_b < 800:
        fundo.blit(imagem_barco,(posx_b,posy))
        fundo.blit(imagem_canibal1,(posx_c1,500))
        fundo.blit(imagem_canibal2,(posx_c2,500))
        posx_b = posx_b + velocidade
        posx_c1 = posx_c1 + velocidade
        posx_c2 = posx_c2 + velocidade
        pygame.display.update( )
        carregarFundo()

def desloc5():
    desloc4()
    posx_b = 800
    posx_c = 860
    def carregarFundo():
        fundo.fill(branco)
        fundo.blit(imagem_rio, (0, 0))
        fundo.blit(imagem_missionario1,(1,400))
        fundo.blit(imagem_missionario2,(60,400))
        fundo.blit(imagem_missionario3,(120,400))
        fundo.blit(imagem_canibal2,(1070,400))
        fundo.blit(imagem_canibal3,(1145,400))
    carregarFundo()
    while posx_b > 230:
        fundo.blit(imagem_barco,(posx_b,posy))
        fundo.blit(imagem_canibal1,(posx_c,500))
        posx_b = posx_b - velocidade
        posx_c = posx_c - velocidade
        pygame.display.update( )
        carregarFundo()

def desloc6():
    desloc5()
    posx_b = 230
    posx_m1 = 260
    posx_m2 = 340
    def carregarFundo():
        fundo.fill(branco)
        fundo.blit(imagem_rio, (0, 0))
        fundo.blit(imagem_missionario1,(1,400))
        fundo.blit(imagem_canibal1,(190,400))
        fundo.blit(imagem_canibal2,(1070,400))
        fundo.blit(imagem_canibal3,(1145,400))
    carregarFundo()
    while posx_b < 800:
        fundo.blit(imagem_barco,(posx_b,posy))
        fundo.blit(imagem_missionario2,(posx_m1,500))
        fundo.blit(imagem_missionario3,(posx_m2,500))
        posx_b = posx_b + velocidade
        posx_m1 = posx_m1 + velocidade
        posx_m2 = posx_m2 + velocidade
        pygame.display.update()
        carregarFundo()


def desloc7():
    desloc6()
    posx_b = 800
    posx_m = 860
    posx_c = 940
    def carregarFundo():
        fundo.fill(branco)
        fundo.blit(imagem_rio, (0, 0))
        fundo.blit(imagem_missionario1,(1,400))
        fundo.blit(imagem_canibal1,(190,400))
        fundo.blit(imagem_missionario3,(800,400))
        fundo.blit(imagem_canibal3,(1145,400))
    carregarFundo()
    while posx_b > 230:
        fundo.blit(imagem_barco,(posx_b,posy))
        fundo.blit(imagem_missionario3,(posx_m,500))
        fundo.blit(imagem_canibal2,(posx_c,500))
        posx_b = posx_b - velocidade
        posx_m = posx_m - velocidade
        posx_c = posx_c - velocidade
        pygame.display.update( )
        carregarFundo()

def desloc8():
    desloc7()
    posx_b = 230
    posx_m1 = 260
    posx_m2 = 340
    def carregarFundo():
        fundo.fill(branco)
        fundo.blit(imagem_rio, (0, 0))
        fundo.blit(imagem_missionario3,(800,400))
        fundo.blit(imagem_canibal1,(190,400))
        fundo.blit(imagem_canibal2,(330,400))
        fundo.blit(imagem_canibal3,(1145,400))
    carregarFundo()
    while posx_b < 800:
        fundo.blit(imagem_barco,(posx_b,posy))
        fundo.blit(imagem_missionario2,(posx_m1,500))
        fundo.blit(imagem_missionario3,(posx_m2,500))
        posx_b = posx_b + velocidade
        posx_m1 = posx_m1 + velocidade
        posx_m2 = posx_m2 + velocidade
        pygame.display.update()
        carregarFundo()


def desloc9():
    desloc8()
    posx_b = 800
    posx_c = 860
    def carregarFundo():
        fundo.fill(branco)
        fundo.blit(imagem_rio, (0, 0))
        fundo.blit(imagem_missionario1,(930,400))
        fundo.blit(imagem_missionario2,(865,400))
        fundo.blit(imagem_missionario3,(800,400))
        fundo.blit(imagem_canibal1,(190,400))
        fundo.blit(imagem_canibal3,(330,400))
    carregarFundo()
    while posx_b > 230:
        fundo.blit(imagem_barco,(posx_b,posy))
        fundo.blit(imagem_canibal2,(posx_c,500))
        posx_b = posx_b - velocidade
        posx_c = posx_c - velocidade
        pygame.display.update( )
        carregarFundo()

def desloc10():
    desloc9()
    posx_b = 230
    posx_c1 = 260
    posx_c2 = 340
    def carregarFundo():
        fundo.fill(branco)
        fundo.blit(imagem_rio, (0, 0))
        fundo.blit(imagem_missionario1,(930,400))
        fundo.blit(imagem_missionario2,(865,400))
        fundo.blit(imagem_missionario3,(800,400))
        fundo.blit(imagem_canibal3,(330,400))
    carregarFundo()
    while posx_b < 800:
        fundo.blit(imagem_barco,(posx_b,posy))
        fundo.blit(imagem_canibal1,(posx_c1,500))
        fundo.blit(imagem_canibal2,(posx_c2,500))
        posx_b = posx_b + velocidade
        posx_c1 = posx_c1 + velocidade
        posx_c2 = posx_c2 + velocidade
        pygame.display.update( )
        carregarFundo()

def desloc11():
    desloc10()
    posx_b = 800
    posx_c = 860
    def carregarFundo():
        fundo.fill(branco)
        fundo.blit(imagem_rio, (0, 0))
        fundo.blit(imagem_missionario1,(930,400))
        fundo.blit(imagem_missionario2,(865,400))
        fundo.blit(imagem_missionario3,(800,400))
        fundo.blit(imagem_canibal1,(995,400))
        fundo.blit(imagem_canibal3,(330,400))
    carregarFundo()
    while posx_b > 230:
        fundo.blit(imagem_barco,(posx_b,posy))
        fundo.blit(imagem_canibal2,(posx_c,500))
        posx_b = posx_b - velocidade
        posx_c = posx_c - velocidade
        pygame.display.update( )
        carregarFundo()

def desloc12():
    desloc11()
    posx_b = 230
    posx_c1 = 260
    posx_c2 = 340
    def carregarFundo():
        fundo.fill(branco)
        fundo.blit(imagem_rio, (0, 0))
        fundo.blit(imagem_missionario1,(930,400))
        fundo.blit(imagem_missionario2,(865,400))
        fundo.blit(imagem_missionario3,(800,400))
        fundo.blit(imagem_canibal1,(995,400))
    carregarFundo()
    while posx_b < 800:
        fundo.blit(imagem_barco,(posx_b,posy))
        fundo.blit(imagem_canibal2,(posx_c1,500))
        fundo.blit(imagem_canibal3,(posx_c2,500))
        posx_b = posx_b + velocidade
        posx_c1 = posx_c1 + velocidade
        posx_c2 = posx_c2 + velocidade
        pygame.display.update( )
        carregarFundo()

def desloc13():
    desloc12()
    fundo.fill(branco)
    fundo.blit(imagem_rio, (0, 0))
    fundo.blit(imagem_missionario1,(930,400))
    fundo.blit(imagem_missionario2,(865,400))
    fundo.blit(imagem_missionario3,(800,400))
    fundo.blit(imagem_canibal1,(995,400))
    fundo.blit(imagem_canibal2,(1070,400))
    fundo.blit(imagem_canibal3,(1145,400))                 
    fundo.blit(imagem_barco,(800,posy))
def fim():
    fundo.fill(branco)
    fundo.blit(imagem_rio, (0, 0))
    fundo.blit(imagem_missionario1,(930,400))
    fundo.blit(imagem_missionario2,(865,400))
    fundo.blit(imagem_missionario3,(800,400))
    fundo.blit(imagem_canibal1,(995,400))
    fundo.blit(imagem_canibal2,(1070,400))
    fundo.blit(imagem_canibal3,(1145,400))                 
    fundo.blit(imagem_barco,(800,posy))
    

fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Missionarios e Canibais")

imagem_rio = pygame.image.load('rio1.png') 
imagem_missionario1 = pygame.image.load('missionario1.jpg')
imagem_missionario2 = pygame.image.load('missionario1.jpg')
imagem_missionario3 = pygame.image.load('missionario1.jpg')
imagem_canibal1 =  pygame.image.load('canibal1.png')
imagem_canibal2 =  pygame.image.load('canibal1.png')
imagem_canibal3 =  pygame.image.load('canibal1.png')
imagem_barco = pygame.image.load('barco1.jpg')

resultado = MissionariosCanibais1.busca(MissionariosCanibais1.estadoInicial)
print(len(resultado))

def main():
    pygame.font.init()
    font = pygame.font.SysFont('Calibri', 100, True, False)
    text = font.render('INICIAR', True, preto)
    
    sair = True

    while sair:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sair = False

        fundo.fill(branco)
        fundo.blit(imagem_rio, (0, 0))
        fundo.blit(imagem_missionario1,(1,400))
        fundo.blit(imagem_missionario2,(60,400))
        fundo.blit(imagem_missionario3,(120,400))
        fundo.blit(imagem_canibal1,(190,400))
        fundo.blit(imagem_canibal2,(260,400))
        fundo.blit(imagem_canibal3,(330,400))
        fundo.blit(imagem_barco,(posx,posy))

        
        botao = pygame.draw.rect(fundo, branco, [pos_x-160, pos_y, 320,80] )
        fundo.blit(text, [pos_x-160,pos_y])
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if (botao[0] <= x <= botao[0]+320) and (botao[1] <= y <= botao[1]+80):
                desloc13()        
                fim()
                break
        pygame.display.update( )
            
        
    pygame.display.quit()
    quit()

main()
