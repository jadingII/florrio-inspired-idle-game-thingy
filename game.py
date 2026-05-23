import pygame
import random

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("placeholder name")

#button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        #draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


# load an image of the main menu cuz im too lazy to make one
mainMenuImg = pygame.transform.scale_by(pygame.image.load("mainmenu.png").convert_alpha(), 0.5)
common = pygame.transform.scale_by(pygame.image.load("commonbutton.png").convert_alpha(), 0.41)
unusual = pygame.transform.scale_by(pygame.image.load("unusual.png").convert_alpha(), 0.41)

#create buttons
commonButton = Button(29, 341, common)
unusualButton = Button(91, 341, unusual)

#game loop
def main():
    run = True
    commonMenuOpen = False
    unusualMenuOpen = False

    while run:

        screen.fill((255, 255, 255))

        screen.blit(mainMenuImg, (0, 0))
        if commonButton.draw():
            if commonMenuOpen == True:
                commonMenuOpen = False
                print("common menu closed")
            else:
                commonMenuOpen = True
                if unusualMenuOpen == True:
                    unusualMenuOpen = False
                    print("unusual menu closed")
                print("common menu opened")
        if unusualButton.draw():
            if unusualMenuOpen == True:
                unusualMenuOpen = False
                print("unusual menu closed")
            else:
                unusualMenuOpen = True
                if commonMenuOpen == True:
                    commonMenuOpen = False
                    print("common menu closed")
                print("unusual menu opened")

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