import pygame
import sys
from grid import *

star_grid = GridMatrix(500, 500)
rect_list = star_grid.create_rects()
white = [255, 255, 255]
black = [0, 0, 0]
blue = [0, 0, 255]

screen = pygame.display.set_mode([star_grid.width, star_grid.height])
pygame.display.set_caption("A* path finder")

for square_obj in rect_list:
    square_obj['screen'] = screen
    square_obj['color'] = black


def change_color(some_list):
    for item in rect_list:
        for coord in some_list:
            if item['coord'] == coord:
                item['color'] = blue
                item['fill'] = 0


def main():
    pygame.init()
    return_to_parse = []
    while 1:
        screen.fill(white)
        pointer_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            for n in rect_list:
                my_rectal = pygame.Rect(n['grid'])
                pygame.draw.rect(n['screen'], n['color'], n['grid'], n['fill'])

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if my_rectal.collidepoint(pointer_pos):
                            n['fill'] = 0
                            return_to_parse = star_grid.find_nine(n['coord'], n['color'])
                            change_color(return_to_parse)

            pygame.display.flip()


main()
