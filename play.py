import pygame
import levels
import help

pygame.font.init()

name = pygame.font.SysFont('comicsans', 50)

win_width=1200
win_height=600

black=(0,0,0)
white=(255,255,255)

play_width=120
play_height=100


help_width=50
help_height=50

win=pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Stickman Skate")

play=pygame.transform.scale(pygame.image.load(r"default_images\play.png"),(play_width,play_height))
help=pygame.transform.scale(pygame.image.load(r"default_images\help.png"),(help_width,help_height))

play_hover=pygame.transform.scale(pygame.image.load(r"default_images\play.png"),(play_width+10,play_height+10))
help_hover=pygame.transform.scale(pygame.image.load(r"default_images\help.png"),(help_width+20,help_height+20))

play_rect=pygame.Rect(525,300,play_width,play_height)
help_rect=pygame.Rect(10,150,help_width,help_height)

play_rect_hover=pygame.Rect(520,295,play_width+10,play_height+10)
help_rect_hover=pygame.Rect(8,148,help_width+20,help_height+20)


def window():
    win.fill(white)
    level = name.render("Stickman Skate", 1, black)
    win.blit(level,(400,200))
    win.blit(play,(play_rect.x,play_rect.y))
    win.blit(help,(help_rect.x,help_rect.y))

    pos=pygame.mouse.get_pos()
    if play_rect.collidepoint(pos):
        win.blit(play_hover, (play_rect_hover.x, play_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
           levels.main()

    elif help_rect.collidepoint(pos):
        win.blit(help_hover, (help_rect_hover.x, help_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
           help.main()

    pygame.display.update()

def main():

    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        window()
    pygame.quit()

if __name__=="__main__":
    pygame.init()
    main()