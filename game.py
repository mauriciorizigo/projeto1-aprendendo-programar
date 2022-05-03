

import pygame

pygame.init()
x = 430
y = 200
pos_x = 100
pos_y = 300
velocidade = 10
velocidade_outros = 20
fundo = pygame.image.load('estrada.png')
carro = pygame.image.load('car.png')
policia = pygame.image.load('policia.png')
outro_carro = pygame.image.load('outro_carro.png')



janela = pygame.display.set_mode((800,600))# criando a janela por periodo muito curto

pygame.display.set_caption("Criando um jogo com Python")# titulo na janela
#para manter a janela aberta
janela_aberta = True
while janela_aberta:
    pygame.time.delay(50) #repeticao da imagem em milisegundos

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           janela_aberta = False

    comandos = pygame.key.get_pressed()# quando for acionado alguma tecla e responde
    if comandos[pygame.K_UP]:# caso acionado a tecla pra cima
        y-= velocidade #quando a tecla for para cima sera jogada a imagem - 5 pixels
    if comandos[pygame.K_DOWN]:
        y+= velocidade
    if comandos[pygame.K_RIGHT]:
        x+= velocidade
    if comandos[pygame.K_LEFT]:
        x-= velocidade

    if (pos_y <= -200):# if para ultrapassar a tela 
        pos_y = 600    

    pos_y -= velocidade_outros    

    #janela.fill((0,0,0))# para apagar a imagem a cada movimento
    janela.blit(fundo, (50, 0))
    janela.blit(carro, (x,y))
    janela.blit(policia, (pos_x, pos_y))
    janela.blit(outro_carro, (pos_x +300, pos_y))

    

# criando um circulo com rgb na metade da tela com 50 de circunferencia,raio de pixel
    #pygame.draw.circle(janela, (0,255,0), (x, y),50)
    pygame.display.update()#atualizando a tela 

pygame.quit()












