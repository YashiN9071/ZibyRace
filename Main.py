import pygame

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)

fps = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("black"))
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
