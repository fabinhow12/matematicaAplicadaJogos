import pygame
import math
from pygame.locals import *


pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width,height))#seta tamanho da tela


keys = [False,False,False,False]
playerpos = [300,300]
pygame.mixer.init()
pygame.display.set_caption("X: "+str(playerpos[0])+", "+"Y: "+str(playerpos[1]))#Seta o titulo da tela

#Carrega as imagens

player = pygame.image.load("images/dude.png")
grass = pygame.image.load("images/grass.png")

#Carrega o audio
pygame.mixer.music.load("audio/moonlight.wav")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)


running = 1
exitcode = 0
while running:

    #limpa a tela antes de desenhar
    screen.fill(0)

    #seta o grass em toda tela
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))

    #Desenha o player
    screen.blit(player,playerpos)

    # Atualiza A Tela
    pygame.display.flip()

    # 8 - loop para pegar os eventos do teclado
    for event in pygame.event.get():
        # ve se foi pressionado o x da tela
        if event.type==pygame.QUIT:
            # fecha o jogo
            pygame.quit()
            exit(exitcode)
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False


    #move o player
    if (playerpos[0] > 0 or playerpos[0] <800):
        if keys[0]:
            playerpos[1]-=5
            pygame.display.set_caption("X: "+str(playerpos[0])+", "+"Y: "+str(playerpos[1]))
        elif keys[2]:
            playerpos[1]+=5
            pygame.display.set_caption("X: "+str(playerpos[0])+", "+"Y: "+str(playerpos[1]))
        if keys[1]:
            playerpos[0]-=5
            pygame.display.set_caption("X: "+str(playerpos[0])+", "+"Y: "+str(playerpos[1]))
        elif keys[3]:
            playerpos[0]+=5
            pygame.display.set_caption("X: "+str(playerpos[0])+", "+"Y: "+str(playerpos[1]))


