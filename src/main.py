# from akiba import *
import pygame
import mouse
import image
import fox
from const import *
import os
import sys

pygame.init()

DS = pygame.display.set_mode(ScreenSize)
pygame.display.set_icon(pygame.image.load("pic/icon/fox-tail2.png"))
pygame.display.set_caption("akiba!")

Background = image.Image("pic/background/snowland1.png", 0, (0, 0), ScreenSize)
Fox2 = fox.Fox(WALK, (100, 500))
# Fox3 = fox.Fox(SLEEP, (500, 500))
UserMouse = mouse.Mouse()

flag1 = 0
d1 = (500, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    DS.fill((255, 255, 255))
    Background.draw(DS)
    UserMouse.UpdateIsPressed()
    if UserMouse.IsLeftPressed:
        d1 = (UserMouse.GetXpos(), UserMouse.GetYpos())
    # if pygame.mouse.get_pressed()[0]:
    #     d1 = (pygame.mouse.get_pos()[0] - 64, 500)
    Fox2.FoxCheck(d1)
    Fox2.FoxUpdate()
    Fox2.draw(DS)

    pygame.display.update()
    pygame.time.Clock().tick(fps / Foxtick)
