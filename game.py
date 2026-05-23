from turtle import Screen

import pygame
import random

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("placeholder name")

# load an image of the main menu cuz im too lazy to make one
mainMenuImg = pygame.transform.scale_by(pygame.image.load("mainmenu.png").convert_alpha(), 0.5)
commonImg = pygame.transform.scale_by(pygame.image.load("commonbutton.png").convert_alpha(), 0.41)
unusualImg = pygame.transform.scale_by(pygame.image.load("unusual.png").convert_alpha(), 0.41)

#button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        #draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

#create buttons
common = Button(29, 341, commonImg)
unusual = Button(91, 341, unusualImg)

#game loop
def main():
    run = True
    while run:

        screen.fill((255, 255, 255))

        screen.blit(mainMenuImg, (0, 0))
        common.draw()
        unusual.draw()


        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False
                break

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()