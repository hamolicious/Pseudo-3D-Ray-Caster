
import pygame
from world_manager import generate_world

pygame.init()
size = (1000, 500)
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
pygame.display.set_icon(screen)
pygame.display.set_caption('Ray Cast')
clock, fps = pygame.time.Clock(), 30

world, player = generate_world((500, 500))

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

    for rect in world:
        pygame.draw.rect(screen, [255, 255, 255], rect)
    player.draw_ray_cast(screen, world)
    player.show(screen)

    pygame.display.update()
    clock.tick(fps)

