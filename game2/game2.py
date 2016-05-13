import pygame
import math
from pygame.locals import *


pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width,height))#seta tamanho da tela


keys = [False,False,False,False]
playerpos = [300,300]
arrows=[]#Armezena os tiros
pygame.mixer.init()
pygame.display.set_caption("X: "+str(playerpos[0])+", "+"Y: "+str(playerpos[1]))#Seta o titulo da tela

#Carrega as imagens

player = pygame.image.load("images/dude.png")
grass = pygame.image.load("images/grass.png")
arrow = pygame.image.load("images/bullet.png")

#Carrega o audio
shoot = pygame.mixer.Sound("audio/shoot.wav")
pygame.mixer.music.load("audio/moonlight.wav")
shoot.set_volume(0.05)
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

    #Desenha o player e define a rotacao
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)

    #Desenha os tiros
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))


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
        if event.type==pygame.MOUSEBUTTONDOWN:
            shoot.play()
            position=pygame.mouse.get_pos()
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])

    #move o player

    if keys[0]:
        if playerpos[1] >0:
            playerpos[1]-=5
            pygame.display.set_caption("X: "+str(playerpos[0])+", "+"Y: "+str(playerpos[1]))
    elif keys[2]:
        if playerpos[1] <600:
            playerpos[1]+=5
            pygame.display.set_caption("X: "+str(playerpos[0])+", "+"Y: "+str(playerpos[1]))
    if keys[1]:
        if playerpos[0] > 0:
            playerpos[0]-=5
            pygame.display.set_caption("X: "+str(playerpos[0])+", "+"Y: "+str(playerpos[1]))
    elif keys[3]:
        if playerpos[0] < 800:
            playerpos[0]+=5
            pygame.display.set_caption("X: "+str(playerpos[0])+", "+"Y: "+str(playerpos[1]))


