import pygame

pygame.init()

dis = pygame.display.set_mode((500, 500))
x = 50
y = 50
height = 40
width = 100
run = True
vel = 10
clock = pygame.time.Clock()
direction = 'Right'

def animate2(x, y):
    if y <= 120 and x < 120:
        x += 5
        pygame.draw.rect(dis, (255, 0, 0), pygame.Rect(x, y, 20, 20))
    elif x >= 120 and y < 160:
        y += 5
        pygame.draw.rect(dis, (255, 0, 0), pygame.Rect(x, y, 20, 20))
    elif y >= 160 and x > 80:
        x -= 5
        pygame.draw.rect(dis, (255, 0, 0), pygame.Rect(x, y, 20, 20))
    elif x >= 80 and y >= 80:
        y -= 5
        pygame.draw.rect(dis, (255, 0, 0), pygame.Rect(x, y, 20, 20))

    return x, y

def animate(x, y, height, width, direction):
    if x < 0:
        direction = 'Right'

    elif x > 400:
        direction = 'Left'

    if direction == 'Right':
        x += vel

    elif direction == 'Left':
        x -= vel

    pygame.draw.rect(dis, (255, 0, 0), pygame.Rect(x, y, width, height))

    return x, direction


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    dis.fill((0, 0, 0))

    x, y = animate2(x, y)

   # x, direction = animate(x, y, height, width, direction)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
