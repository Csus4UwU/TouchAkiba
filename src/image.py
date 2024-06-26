import pygame
from const import *
import time


class Image(pygame.sprite.Sprite):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0) -> None:
        self.pathFmt = pathFmt
        self.pathIndex = pathIndex
        self.pathIndexCount = pathIndexCount
        self.pos = list(pos)
        self.size = size
        self.Xrev = False
        self.Yrev = False
        self.UpdateImage()

    def UpdateImage(self):
        path = self.pathFmt
        if self.pathIndexCount != 0:
            path = path % self.pathIndex
        self.image = pygame.image.load(path)
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)
        if self.Xrev or self.Yrev:
            self.image = pygame.transform.flip(self.image, self.Xrev, self.Yrev)

    def UpdateIndex(self, pathIndex):
        self.pathIndex = pathIndex
        self.UpdateImage()

    def UpdatePath(self, pathFmt, pathIndexCount):
        if pathFmt != self.pathFmt:
            self.pathIndex = 1
        self.pathFmt = pathFmt
        self.pathIndexCount = pathIndexCount
        self.UpdateImage()

    def UpdateSize(self, size):
        self.size = size
        self.UpdateImage()

    def CheckImageIndex(self):
        idx = (self.pathIndex + 1) % self.pathIndexCount
        self.UpdateIndex(idx)

    def CheckPosition(self, speed):
        self.pos[0] += speed[0]
        self.pos[1] += speed[1]

    def LocLimit(self):
        for i in range(2):
            if self.pos[i] > ScreenSize[i]:
                self.pos[i] = ScreenSize[i]
            if self.pos[i] < 0:
                self.pos[i] = 0

    def Update(self, speed, path, idxcount):
        self.UpdatePath(path, idxcount)
        self.CheckImageIndex()
        self.CheckPosition(speed)
        self.LocLimit()

    def GetRect(self):
        rect = self.image.get_rect()
        rect.x, rect.y = self.pos
        return rect

    def XReverse(self):
        self.Xrev = True

    def draw(self, ds):
        ds.blit(self.image, self.GetRect())
