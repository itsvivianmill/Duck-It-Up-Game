import pygame
from homepagebutton import homepageButtons
pygame.init()

def get_font(size):
    return pygame.font.Font('PressStart2P-Regular.ttf', size)

PLAY_Button= homepageButtons(image=pygame.image.load("transparent.png"), pos=(400, 300), 
                    text_input="-> play!", font=get_font(45), base_color="white", hovering_color="black")
QUIT_Button= homepageButtons(image=pygame.image.load("transparent.png"), pos=(300, 550), 
                    text_input="quit", font=get_font(20), base_color="white", hovering_color="white")

BG = pygame.image.load("background.png")
def draw_start_menu(SCREEN):
    SCREEN.blit(BG,(0,0))

    MENU_TEXT = get_font(55).render('DUCK IT UP', True, (58, 0, 205))
    MENU_RECT = MENU_TEXT.get_rect(center = (300,175))

    SCREEN.blit(MENU_TEXT, MENU_RECT)

    for button in [PLAY_Button, QUIT_Button]:
        button.changeColor(pygame.mouse.get_pos())
        button.update(SCREEN)
        

    



