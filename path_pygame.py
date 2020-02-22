import pygame
import sys
from grid import *

pygame.init()

# set global declarations
tracker = [0, 1]
star_grid = GridMatrix(700, 700)
rect_list = star_grid.create_rects()
colors = {
    'white': [255, 255, 255],
    'black': [0, 0, 0],
    'red': [255, 0, 0],
    'green': [134, 168, 109]
}
screen = pygame.display.set_mode([star_grid.width, star_grid.height])
pygame.display.set_caption("A* path finder")

# sets dict values from None passed
for square_obj in rect_list:
    square_obj['screen'] = screen
    square_obj['color'] = colors['black']

# tracks previous current square
cache = []


def draw(x, y, big_list, col):
    for g in big_list:
        if g['coord'] == [x, y]:
            g['color'] = col
            g['fill'] = 0


def maffs(x, y, col, pointer, track):
    a, b = pointer

    if a < 20 and b < 20:
        x, y = 0, 0
        draw(x, y, rect_list, col)
        tracker[track] = [x, y]
        return True
    else:
        a_div = divmod(a, 20)
        b_div = divmod(b, 20)
        x = (a - a_div[1]) // 20
        y = (b - b_div[1]) // 20
        draw(x, y, rect_list, col)
        tracker[track] = [x, y]
        print(tracker)
        return True


# path logic for finding route from current to tracker[1]
def path_logic(current_rect):
    global cache
    global tracker
    global rect_list
    val_check = []

    color_carrier = find_nine(current_rect, rect_list)

    for coords in color_carrier:
        x1, y1 = coords['coord']
        x2, y2 = tracker[1]
        dist = round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 3)
        val_check.append([coords['coord'], dist])

    v = min(val_check, key=lambda misc: misc[1])
    for item in color_carrier:
        if item['coord'] == cache:
            draw(item['coord'][0], item['coord'][1], rect_list, colors['black'])
        else:
            draw(item['coord'][0], item['coord'][1], rect_list, colors['green'])

    cache = tracker[0]
    tracker[0] = v[0]


if __name__ == '__main__':
    clock = pygame.time.Clock()
    start = [False, False, False]
    x = 0
    y = 0
    running = True

    while running:

        screen.fill(colors['white'])
        pointer_pos = pygame.mouse.get_pos()

        for n in rect_list:
            pygame.draw.rect(n['screen'], n['color'], n['grid'], n['fill'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not start[0]:
                start[0] = maffs(x, y, colors['black'], pointer_pos, 0)
            elif event.type == pygame.MOUSEBUTTONDOWN and not start[1]:
                start[1] = maffs(x, y, colors['red'], pointer_pos, 1)

        if start[0] and start[1] and not start[2]:
            print(tracker)
            path_logic(tracker[0])
            if tracker[0] == tracker[1]:
                start[2] = True

        pygame.display.update()
        clock.tick(30)
pygame.quit()
