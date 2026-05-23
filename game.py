import pygame
import random
import button

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("placeholder name")

# load an image of the main menu cuz im too lazy to make one
mainMenuImg = pygame.transform.scale_by(pygame.image.load("mainmenu.png").convert_alpha(), 0.5)
common = pygame.transform.scale_by(pygame.image.load("commonbutton.png").convert_alpha(), 0.41)
unusual = pygame.transform.scale_by(pygame.image.load("unusual.png").convert_alpha(), 0.41)

#create buttons
commonButton = button.Button(29, 341, common)
unusualButton = button.Button(91, 341, unusual)

#game loop
def main():
    run = True
    commonMenuOpen = False
    unusualMenuOpen = False

    while run:

        screen.fill((255, 255, 255))

        screen.blit(mainMenuImg, (0, 0))
        if commonButton.draw(screen):
            if commonMenuOpen == True:
                commonMenuOpen = False
                print("common menu closed")
            else:
                commonMenuOpen = True
                if unusualMenuOpen == True:
                    unusualMenuOpen = False
                    print("unusual menu closed")
                print("common menu opened")
        if unusualButton.draw(screen):
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