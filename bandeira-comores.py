import math
import sys

import pygame
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))

def drawStar(screen, color, position, size, angle):
    points = []
    x, y = position

    for i in range(5):
        pointX = x - size * math.cos((2 * math.pi) * (i / 5) + (math.pi / 2) + angle * math.pi / 180)
        pointY = y - size * math.sin((2 * math.pi) * (i / 5) + (math.pi / 2) + angle * math.pi / 180) 
        
        point = (pointX, pointY)
        points.append(point)

        innerPointX = x - size / 3 * math.cos((2 * math.pi) * (i / 5) + (math.pi / 2) + (2 * math.pi / 10) + angle * math.pi / 180)
        innerPointY = y - size / 3 * math.sin((2 * math.pi) * (i / 5) + (math.pi / 2) + (2 * math.pi / 10) + angle * math.pi / 180)

        innerPoint = (innerPointX, innerPointY)
        points.append(innerPoint)

    pygame.draw.polygon(screen, color, points)

while True:
    pygame.draw.rect(
        DISPLAYSURF,
        (255, 210, 0),
        pygame.Rect(0, 0, 300, 50)
    )

    pygame.draw.rect(
        DISPLAYSURF,
        (255, 255, 255),
        pygame.Rect(0, 50, 300, 50)
    )

    pygame.draw.rect(
        DISPLAYSURF,
        (239, 48, 62),
        pygame.Rect(0, 100, 300, 50)
    )

    pygame.draw.rect(
        DISPLAYSURF,
        (0, 58, 166),
        pygame.Rect(0, 150, 300, 50)
    )

    pygame.draw.polygon(
        DISPLAYSURF,
        (0, 151, 54),
        [
            (0, 0),
            (150, 100),
            (0, 200)
        ]
    )

    pygame.draw.circle(
        DISPLAYSURF,
        (255, 255, 255),
        (50, 100),
        45
    )

    pygame.draw.circle(
        DISPLAYSURF,
        (0, 151, 54),
        (65, 100),
        45
    )

    drawStar(
        DISPLAYSURF,
        (255, 255, 255),
        (55, 70),
        7.5,
        0
    )

    drawStar(
        DISPLAYSURF,
        (255, 255, 255),
        (55, 90),
        8,
        0
    )

    drawStar(
        DISPLAYSURF,
        (255, 255, 255),
        (55, 110),
        8,
        0
    )

    drawStar(
        DISPLAYSURF,
        (255, 255, 255),
        (55, 130),
        8,
        0
    )

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
