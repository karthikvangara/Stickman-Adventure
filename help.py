import pygame
import play

pygame.font.init()

win_width=1200
win_height=600

pic_width=200
pic_height=200

back_width=50
back_height=50

black=(0,0,0)
white=(255,255,255)

font=pygame.font.SysFont("comicsans",20)

win=pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Help")

pic=pygame.transform.scale(pygame.image.load(r"D:\my games\stickman\help\pic.jpg"),(pic_width,pic_height))
back=pygame.transform.scale(pygame.image.load(r"D:\my games\stickman\default_images\Back.png"),(back_width,back_height))
back_hover=pygame.transform.scale(pygame.image.load(r"D:\my games\stickman\default_images\Back.png"),(back_width+10,back_height+10))

back_rect=pygame.Rect(575,50,back_width,back_height)
back_rect_hover=pygame.Rect(573,48,back_width+10,back_height+10)

def window():
    win.fill(white)
    win.blit(back,(back_rect.x,back_rect.y))

    pos = pygame.mouse.get_pos()

    if back_rect.collidepoint(pos):
        win.blit(back_hover, (back_rect_hover.x, back_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
            play.main()

    win.blit(pic,(500,150))

    text=font.render("@ Karthik Vangara",1,black)
    win.blit(text,(510,400))

    text=font.render("Use Arrow Keys to move left and right",1,black)
    win.blit(text,(450,450))

    text=font.render("Use SpaceBar to jump",1,black)
    win.blit(text,(500,500))

    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window()
    pygame.quit()

if __name__=="__main__":
    main()