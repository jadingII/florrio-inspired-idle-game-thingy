# imports
import pygame
import random
import button
import craft

pygame.init()

WIDTH, HEIGHT = 1300, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("placeholder name")

# load an images cuz im too lazy to make one
mainMenuImg = pygame.transform.scale_by(pygame.image.load("images/mainmenu.png").convert_alpha(), 1.3)
common = pygame.transform.scale_by(pygame.image.load("images/commonbutton.png").convert_alpha(), 0.42)
unusual = pygame.transform.scale_by(pygame.image.load("images/unusual.png").convert_alpha(), 0.42)
rare = pygame.transform.scale_by(pygame.image.load("images/rare.png").convert_alpha(), 0.42)
epic = pygame.transform.scale_by(pygame.image.load("images/epic.png").convert_alpha(), 0.42)
legendary = pygame.transform.scale_by(pygame.image.load("images/legendary.png").convert_alpha(), 0.42)
mythic = pygame.transform.scale_by(pygame.image.load("images/mythic.png").convert_alpha(), 0.42)
ultra = pygame.transform.scale_by(pygame.image.load("images/ultra.png").convert_alpha(), 0.42)
super = pygame.transform.scale_by(pygame.image.load("images/super.png").convert_alpha(), 0.42)
eternal = pygame.transform.scale_by(pygame.image.load("images/eternal.png").convert_alpha(), 0.42)

#create buttons
commonButton = button.Button(28, 361, common)
unusualButton = button.Button(94, 361, unusual)
rareButton = button.Button(160, 361, rare)
epicButton = button.Button(228, 361, epic)
legendaryButton = button.Button(294, 361, legendary)
mythicButton = button.Button(360, 361, mythic)
ultraButton = button.Button(430, 361, ultra)
superButton = button.Button(496, 361, super)
eternalButton = button.Button(562, 361, eternal)

#stuffs for text

#define font sizes
size_petals = 10
size_menu = 30

#define fonts
FONT_petals = pygame.font.SysFont("comicsans", size_petals)
FONT_menuHeader = pygame.font.SysFont("comicsans", size_menu)
FONT_menuText = pygame.font.SysFont("comicsans", size_menu - 10)

#define colours
TEXT_WHITE = (255, 255, 255)
TEXT_BLACK = (0, 0, 0)

#text
def draw_text(text, font, text_col , x, y):
    TEXT = font.render(text, True, text_col)
    screen.blit(TEXT, (x, y))

#game loop
def main():
    run = True
    #menu states
    commonMenuOpen = False
    unusualMenuOpen = False
    rareMenuOpen = False
    epicMenuOpen = False
    legendaryMenuOpen = False
    mythicMenuOpen = False
    ultraMenuOpen = False
    superMenuOpen = False
    eternalMenuOpen = False
    #petal amounts
    commonPetals = 0
    unusualPetals = 0
    rarePetals = 0
    epicPetals = 0
    legendaryPetals = 0
    mythicPetals = 0
    ultraPetals = 0
    superPetals = 0
    eternalPetals = 0    
    while run:

        screen.fill((255, 255, 255))

        screen.blit(mainMenuImg, (-917, -380))
        #buttons
        if commonButton.draw(screen):
            if pygame.key.get_pressed()[pygame.K_LSHIFT] == 1 or pygame.key.get_pressed()[pygame.K_RSHIFT] == 1:
                craft.Craft(commonPetals, 0)
                unusualPetals += craft.Craft(commonPetals, 0)[0]
                commonPetals = craft.Craft(commonPetals, 0)[1]
                print("crafting commons...")
            else:
                if commonMenuOpen == True:
                    commonMenuOpen = False
                    print("common menu closed")
                else:
                    commonMenuOpen = True
                    unusualMenuOpen = False
                    rareMenuOpen = False
                    epicMenuOpen = False
                    legendaryMenuOpen = False
                    mythicMenuOpen = False
                    ultraMenuOpen = False
                    superMenuOpen = False
                    eternalMenuOpen = False
                    print("common menu opened")
        if unusualButton.draw(screen) and unusualPetals >= 1:
            if pygame.key.get_pressed()[pygame.K_LSHIFT] == 1 or pygame.key.get_pressed()[pygame.K_RSHIFT] == 1:
                craft.Craft(unusualPetals, 1)
                rarePetals += craft.Craft(unusualPetals, 1)[0]
                unusualPetals = craft.Craft(unusualPetals, 1)[1]
                print("crafting unusuals...")
            else:
                if unusualMenuOpen == True:
                    unusualMenuOpen = False
                    print("unusual menu closed")
                else:
                    unusualMenuOpen = True
                    commonMenuOpen = False
                    rareMenuOpen = False
                    epicMenuOpen = False
                    legendaryMenuOpen = False
                    mythicMenuOpen = False
                    ultraMenuOpen = False
                    superMenuOpen = False
                    eternalMenuOpen = False
                    print("unusual menu opened")
        elif unusualButton.draw(screen) == "craft" and unusual >= 5:
            craft.Craft(unusualPetals, 1)
            rarePetals += craft.Craft(unusualPetals, 1)[0]
            unusualPetals = craft.Craft(unusualPetals, 1)[1]
            print("crafting unusual...")
        if rareButton.draw(screen) and rarePetals >= 1:
            if pygame.key.get_pressed()[pygame.K_LSHIFT] == 1 or pygame.key.get_pressed()[pygame.K_RSHIFT] == 1:
                craft.Craft(rarePetals, 2)
                epicPetals += craft.Craft(rarePetals, 2)[0]
                rarePetals = craft.Craft(rarePetals, 2)[1]
                print("crafting rares...")
            else:
                if rareMenuOpen == True:
                    rareMenuOpen = False
                    print("rare menu closed")
                else:
                    rareMenuOpen = True
                    commonMenuOpen = False
                    unusualMenuOpen = False
                    epicMenuOpen = False
                    legendaryMenuOpen = False
                    mythicMenuOpen = False
                    ultraMenuOpen = False
                    superMenuOpen = False
                    eternalMenuOpen = False
                    print("rare menu opened")
        if epicButton.draw(screen) and epicPetals >= 1:
            if pygame.key.get_pressed()[pygame.K_LSHIFT] == 1 or pygame.key.get_pressed()[pygame.K_RSHIFT] == 1:
                craft.Craft(epicPetals, 3)
                legendaryPetals += craft.Craft(epicPetals, 4)[0]
                epicPetals = craft.Craft(epicPetals, 4)[1]
                print("crafting epics...")
            else:
                if epicMenuOpen == True:
                    epicMenuOpen = False
                    print("epic menu closed")
                else:
                    epicMenuOpen = True
                    commonMenuOpen = False
                    unusualMenuOpen = False
                    rareMenuOpen = False
                    legendaryMenuOpen = False
                    mythicMenuOpen = False
                    ultraMenuOpen = False
                    superMenuOpen = False
                    eternalMenuOpen = False
                    print("epic menu opened")
        if legendaryButton.draw(screen) and legendaryPetals >= 1:
            if pygame.key.get_pressed()[pygame.K_LSHIFT] == 1 or pygame.key.get_pressed()[pygame.K_RSHIFT] == 1:
                craft.Craft(legendaryPetals, 4)
                mythicPetals += craft.Craft(legendaryPetals, 5)[0]
                legendaryPetals = craft.Craft(legendaryPetals, 5)[1]
                print("crafting legendaries...")
            elif legendaryMenuOpen == True:
                legendaryMenuOpen = False
                print("legendary menu closed")
            else:
                legendaryMenuOpen = True
                commonMenuOpen = False
                unusualMenuOpen = False
                rareMenuOpen = False
                epicMenuOpen = False
                mythicMenuOpen = False
                ultraMenuOpen = False
                superMenuOpen = False
                eternalMenuOpen = False
                print("legendary menu opened")
        if mythicButton.draw(screen) and mythicPetals >= 1:
            if pygame.key.get_pressed()[pygame.K_LSHIFT] == 1 or pygame.key.get_pressed()[pygame.K_RSHIFT] == 1:
                craft.Craft(mythicPetals, 5)
                ultraPetals += craft.Craft(mythicPetals, 6)[0]
                mythicPetals = craft.Craft(mythicPetals, 6)[1]
                print("crafting mythics...")
            else:
                if mythicMenuOpen == True:
                    mythicMenuOpen = False
                    print("mythic menu closed")
                else:
                    mythicMenuOpen = True
                    commonMenuOpen = False
                    unusualMenuOpen = False
                    rareMenuOpen = False
                    epicMenuOpen = False
                    legendaryMenuOpen = False
                    ultraMenuOpen = False
                    superMenuOpen = False
                    eternalMenuOpen = False
                    print("mythic menu opened")
        if ultraButton.draw(screen) and ultraPetals >= 1:
            if pygame.key.get_pressed()[pygame.K_LSHIFT] == 1 or pygame.key.get_pressed()[pygame.K_RSHIFT] == 1:
                craft.Craft(ultraPetals, 6)
                superPetals += craft.Craft(ultraPetals, 6)[0]
                ultraPetals = craft.Craft(ultraPetals, 6)[1]
                print("crafting ultras...")
            else:
                if ultraMenuOpen == True:
                    ultraMenuOpen = False
                    print("ultra menu closed")
                else:
                    ultraMenuOpen = True
                commonMenuOpen = False
                unusualMenuOpen = False
                rareMenuOpen = False
                epicMenuOpen = False
                legendaryMenuOpen = False
                mythicMenuOpen = False
                superMenuOpen = False
                eternalMenuOpen = False
                print("ultra menu opened")
        if superButton.draw(screen) and superPetals >= 1:
            if pygame.key.get_pressed()[pygame.K_LSHIFT] == 1 or pygame.key.get_pressed()[pygame.K_RSHIFT] == 1:
                craft.Craft(superPetals, 7)
                eternalPetals += craft.Craft(superPetals, 7)[0]
                superPetals = craft.Craft(superPetals, 7)[1]
                print("crafting supers...")
            else:
                if superMenuOpen == True:
                    superMenuOpen = False
                    print("super menu closed")
                else:
                    superMenuOpen = True
                    commonMenuOpen = False
                    unusualMenuOpen = False
                    rareMenuOpen = False
                    epicMenuOpen = False
                    legendaryMenuOpen = False
                    mythicMenuOpen = False
                    ultraMenuOpen = False
                    eternalMenuOpen = False
                    print("super menu opened")
        if eternalButton.draw(screen) and eternalPetals >= 1:
            if eternalMenuOpen == True:
                eternalMenuOpen = False
                print("eternal menu closed")
            else:
                eternalMenuOpen = True
                commonMenuOpen = False
                unusualMenuOpen = False
                rareMenuOpen = False
                epicMenuOpen = False
                legendaryMenuOpen = False
                mythicMenuOpen = False
                ultraMenuOpen = False
                superMenuOpen = False
                print("eternal menu opened")
        #draw text
        draw_text(f"x{commonPetals}", FONT_petals, TEXT_BLACK, 29, 361)
        draw_text(f"x{unusualPetals}", FONT_petals, TEXT_BLACK, 94, 361)
        draw_text(f"x{rarePetals}", FONT_petals, TEXT_WHITE, 159, 361)
        draw_text(f"x{epicPetals}", FONT_petals, TEXT_WHITE, 229, 361)
        draw_text(f"x{legendaryPetals}", FONT_petals, TEXT_WHITE, 294, 361)
        draw_text(f"x{mythicPetals}", FONT_petals, TEXT_BLACK, 359, 361)
        draw_text(f"x{ultraPetals}", FONT_petals, TEXT_WHITE, 428, 361)
        draw_text(f"x{superPetals}", FONT_petals, TEXT_BLACK, 493, 361)
        draw_text(f"x{eternalPetals}", FONT_petals, TEXT_BLACK, 558, 361)
        #draw menus
        if commonMenuOpen == True:
            pygame.draw.rect(screen, (113, 229, 107), (28, 442, 500, 300))
            draw_text("common", FONT_menuHeader, TEXT_BLACK, 40, 450)
            draw_text("shift click to craft", FONT_menuText, TEXT_BLACK, 40, 500)
        if unusualMenuOpen == True:
            pygame.draw.rect(screen, (221, 220, 95), (28, 442, 500, 300))
            draw_text("unusual", FONT_menuHeader, TEXT_BLACK, 40, 450)
            draw_text("shift click to craft", FONT_menuText, TEXT_BLACK, 40, 500)
        if rareMenuOpen == True:
            pygame.draw.rect(screen, (70, 95, 206), (28, 442, 500, 300))
            draw_text("rare", FONT_menuHeader, TEXT_WHITE, 40, 450)
            draw_text("shift click to craft", FONT_menuText, TEXT_WHITE, 40, 500)
        if epicMenuOpen == True:
            pygame.draw.rect(screen, (134, 33, 223), (28, 442, 500, 300))
            draw_text("epic", FONT_menuHeader, TEXT_WHITE, 40, 450)
            draw_text("shift click to craft", FONT_menuText, TEXT_WHITE, 40, 500)
        if legendaryMenuOpen == True:
            pygame.draw.rect(screen, (222, 32, 32), (28, 442, 500, 300))
            draw_text("legendary", FONT_menuHeader, TEXT_WHITE, 40, 450)
            draw_text("shift click to craft", FONT_menuText, TEXT_WHITE, 40, 500)
        if mythicMenuOpen == True:
            pygame.draw.rect(screen, (33, 219, 223), (28, 442, 500, 300))
            draw_text("mythic", FONT_menuHeader, TEXT_BLACK, 40, 450)
            draw_text("shift click to craft", FONT_menuText, TEXT_BLACK, 40, 500)
        if ultraMenuOpen == True:
            pygame.draw.rect(screen, (254, 43, 117), (28, 442, 500, 300))
            draw_text("ultra", FONT_menuHeader, TEXT_BLACK, 40, 450)
            draw_text("shift click to craft", FONT_menuText, TEXT_BLACK, 40, 500)
        if superMenuOpen == True:
            pygame.draw.rect(screen, (45, 255, 162), (28, 442, 500, 300))
            draw_text("super", FONT_menuHeader, TEXT_BLACK, 40, 450)
            draw_text("shift click to craft", FONT_menuText, TEXT_BLACK, 40, 500)
        if eternalMenuOpen == True:
            pygame.draw.rect(screen, (238, 238, 238), (28, 442, 500, 300))
            draw_text("eternal", FONT_menuHeader, TEXT_WHITE, 40, 450)
            draw_text("shift click to craft", FONT_menuText, TEXT_WHITE, 40, 500)
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