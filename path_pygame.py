import pygame
import sys
from grid import *
import time
import math

# declarations: create grid and colors
star_grid = GridMatrix(700, 700)
rect_list = star_grid.create_rects()
white = [255, 255, 255]
black = [0, 0, 0]
red = [255, 0, 0]
green = [134, 168, 109]
# used to create start and end points for path algorithm
start = [False, False, False]
tracker = [0, 1]

screen = pygame.display.set_mode([star_grid.width, star_grid.height])
pygame.display.set_caption("A* path finder")

# sets dict values from None passed
for square_obj in rect_list:
    square_obj['screen'] = screen
    square_obj['color'] = black

cache = []
def path_logic(current_rect):
    global cache
    global start
    global tracker
    global rect_list
    val_check = []
    color_carrier = find_nine(current_rect)

    if tracker[0] == tracker[1]:
        start[2] = True
    else:
        for coords in color_carrier:
            x1, y1 = coords
            x2, y2 = tracker[1]
            dist = round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 3)
            val_check.append([coords, dist])

        v = min(val_check, key=lambda x: x[1])

        for m in rect_list:
            if m['coord'] == tracker[0]:
                m['color'] = black
                m['fill'] = 0
            else:
                for p in color_carrier:
                    if p == cache:
                        pass
                    elif p == m['coord']:
                        m['color'] = green
                        m['fill'] = 0
        cache = tracker[0]
        tracker[0] = v[0]


def main():
    global tracker
    global debug_counter
    pygame.init()
    while True:
        screen.fill(white)
        pointer_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            global start
            if event.type == pygame.QUIT:
                sys.exit()

            for n in rect_list:
                my_rectal = pygame.Rect(n['grid'])
                pygame.draw.rect(n['screen'], n['color'], n['grid'], n['fill'])

                if not start[0]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if my_rectal.collidepoint(pointer_pos):
                                tracker[0] = (n['coord'])
                                n['fill'] = 0
                                n['color'] = black
                                start[0] = True
                elif not start[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if my_rectal.collidepoint(pointer_pos):
                                tracker[1] = (n['coord'])
                                n['fill'] = 0
                                n['color'] = red
                                start[1] = True
                elif not start[2]:
                    path_logic(tracker[0])
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if my_rectal.collidepoint(5,5):
                                for b in rect_list:
                                    b['color'] = black
                                    b['fill'] = 1
                                start = [False, False, False]
            pygame.display.flip()


if __name__ == '__main__':
    main()
    print("path finder loaded")
