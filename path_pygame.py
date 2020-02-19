import pygame
import sys
from grid import *

# delcarations
star_grid = GridMatrix(500, 500)
rect_list = star_grid.create_rects()
white = [255, 255, 255]
black = [0, 0, 0]
blue = [0, 0, 255]
start = False

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
    while 1:
        screen.fill(white)
        pointer_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            global start
            if event.type == pygame.QUIT:
                sys.exit()

            for n in rect_list:
                my_rectal = pygame.Rect(n['grid'])
                pygame.draw.rect(n['screen'], n['color'], n['grid'], n['fill'])

                if not start:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                                if my_rectal.collidepoint(pointer_pos):
                                    n['fill'] = 0
                                    n['color'] = black
                                    return_to_parse = find_nine(n['coord'], n['color'])
                                    change_color(return_to_parse)
                                    start = True
                else:
                    print("off")

            pygame.display.flip()


main()
