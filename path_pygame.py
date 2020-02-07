import pygame
import sys
from find import logic

def main():
    pygame.init()
    size = width, height = 500, 500
    white = [255, 255, 255]
    green = [64, 191, 128]
    black = [0, 0, 0]
    rectal_list = []

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("A* path finder")
    drag = False

    for i in range(0, (size[0] // 25) + 1):
        for j in range(0, (size[1] // 25) + 1):
            rectal_list.append([screen, black, [0 + j * 25, 1 + i * 25, 26, 26], 1, 0, 0])
    print(rectal_list)

    while 1:
        screen.fill(white)
        pointer_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        for n in range(len(rectal_list)):
            pygame.draw.rect(rectal_list[n][0], rectal_list[n][1], rectal_list[n][2], rectal_list[n][3])
            my_rectal = pygame.Rect(rectal_list[n][2])

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if my_rectal.collidepoint(pointer_pos):
                        drag = True
                        rectal_list[n][3], rectal_list[n][1] = 0, green
                        logic(rectal_list[n])

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drag = False

            elif event.type == pygame.MOUSEMOTION:
                if drag:
                    if my_rectal.collidepoint(pointer_pos):
                        rectal_list[n][3], rectal_list[n][1] = 0, green

        pygame.display.flip()

main()