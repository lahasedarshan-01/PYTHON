import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse Click Counter")


font = pygame.font.SysFont(None, 48)


click_count = 0


running = True
while running:
    screen.fill((255, 255, 255)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_count += 1

    
    text = font.render(f"Your Clicks: {click_count}", True, (0, 0, 0))
    screen.blit(text, (150, 120))

    pygame.display.update()

pygame.quit()
sys.exit()
