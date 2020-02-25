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
    'red2': [235, 64, 52],
    'green': [134, 168, 109]
}
original = []
screen = pygame.display.set_mode([star_grid.width, star_grid.height])
pygame.display.set_caption("A* path finder")

# sets dict values from None passed
for square_obj in rect_list:
    square_obj['screen'] = screen
    square_obj['color'] = colors['black']

# tracks previous current square
cache = [0, 0]


def draw(x, y, big_list, col, wall=None):
    for g in big_list:
        if g['coord'] == [x, y]:
            g['color'] = col
            g['fill'] = 0
            if wall is not None:
                g['wall'] = 1


def draw_grid(col=None):
    if col is None:
        for n in rect_list:
            pygame.draw.rect(n['screen'], n['color'], n['grid'], n['fill'])
    else:
        for n in rect_list:
            n['color'] = colors['black']
            n['fill'] = 1
            pygame.draw.rect(n['screen'], n['color'], n['grid'], n['fill'])


def maffs(x, y, col, pointer, track, wall=None):
    a, b = pointer

    if a < 20 and b < 20:
        x, y = 0, 0
        draw(x, y, rect_list, col, wall)
        tracker[track] = [x, y]
        return True
    else:
        a_div = divmod(a, 20)
        b_div = divmod(b, 20)
        x = (a - a_div[1]) // 20
        y = (b - b_div[1]) // 20
        draw(x, y, rect_list, col, wall)
        tracker[track] = [x, y]
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
        dist = round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)
        if coords['wall'] == 1:
            dist += 100
        elif coords['coord'][0] == cache[0] or coords['coord'][1] == cache[1]:
            dist += 10

        val_check.append([coords['coord'], dist])
    print(val_check)
    v = min(val_check, key=lambda misc: misc[1])
    print(v)
    for item in color_carrier:
        if item['coord'] == cache:
            draw(item['coord'][0], item['coord'][1], rect_list, colors['red2'])
        elif item['coord'] == tracker[1]:
            draw(item['coord'][0], item['coord'][1], rect_list, colors['red'])
        else:
            draw(item['coord'][0], item['coord'][1], rect_list, colors['green'])

    cache = tracker[0]
    tracker[0] = v[0]
    if tracker[0][0] == tracker[1][0] and tracker[0][1] == tracker[1][1]:
        path_logic(tracker[1])
        return True
    else:
        return False


if __name__ == '__main__':
    clock = pygame.time.Clock()
    start = [False, False, False]
    m_trigger = pygame.MOUSEBUTTONDOWN
    dragging = False
    x = 0
    y = 0
    running = True

    while running:

        screen.fill(colors['white'])
        pointer_pos = pygame.mouse.get_pos()

        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == m_trigger and event.button == 3:
                print('right click detected')
                dragging = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    maffs(x, y, colors['black'], pointer_pos, 0, 1)
                    pygame.display.update()
            elif event.type == m_trigger and not start[0]:
                if event.button == 1:
                    original = pointer_pos
                    start[0] = maffs(x, y, colors['black'], pointer_pos, 0)
            elif event.type == m_trigger and not start[1]:
                if event.button == 1:
                    start[1] = maffs(x, y, colors['black'], pointer_pos, 1)
            elif start[0] and start[1] and start[2] and event.type == m_trigger:
                if event.button == 1:
                    start = [False, False, False]
                    draw_grid(1)

        if start[0] and start[1] and not start[2]:
            start[2] = path_logic(tracker[0])

        pygame.display.update()
        clock.tick(30)
pygame.quit()
