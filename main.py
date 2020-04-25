
import pygame
from world_manager import generate_world

pygame.init()
pygame.font.init()
size = (1000, 500)
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
pygame.display.set_icon(screen)
pygame.display.set_caption('Ray Cast')
clock, fps = pygame.time.Clock(), 30

world, player = generate_world((500, 500))

font = pygame.font.SysFont('ariel', 25)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    screen.fill(0)

    player.update(key)
    player.show(screen, world)

    for rect in world:
        pygame.draw.rect(screen, [255, 255, 255], rect)

    button_rect = pygame.Rect(1, 1, 13, 20)
    pygame.draw.rect(screen, [51, 51, 51], button_rect)
    screen.blit(font.render('?', True, [255, 255, 255]), (button_rect[0]+1, button_rect[1]))

    mx, my = mouse_pos
    if button_rect.collidepoint(mx, my):
        pygame.draw.rect(screen, [0, 0, 0], (10, 10, size[0]-20, size[1]-20))
        pygame.draw.rect(screen, [255, 0, 255], (10, 10, size[0]-20, size[1]-20), 3)

        labels = [
            'Move forward   |   W',
            'Move backwards   |   S',
            'Move left   |   A',
            'Move right   |   S',
            'Turn left   |   LEFT',
            'Turn right   |   RIGHT',
            'Turn on low resolution   |   DOWN',
            'Turn on high resolution   |   UP',
        ]

        plane_size = (size[0] - 20, size[1] - 20)
        y = 1
        for lbl in labels:
            lbl = font.render(lbl, True, [255, 255, 255])
            w, h, = lbl.get_size()

            whole_plane = plane_size[1] / len(labels)

            center_x = (plane_size[0]/2 - w/2) + 10
            center_y = (whole_plane * y) - h
            y += 1

            screen.blit(lbl, (center_x, center_y))


    pygame.display.update()
    clock.tick(fps)

