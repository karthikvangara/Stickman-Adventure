import pygame
import levels
import level1
import level2
import level3
import level4
import level5
import level6
import level7

pygame.font.init()

name = pygame.font.SysFont('comicsans', 50)

black=(0,0,0)

win_width=1200
win_height=600

back_width=50
back_height=50

start_width=400
start_height=60

mid_width=1200
mid_height=320

brick_width=200
brick_height=20

win=pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Start")

background=pygame.transform.scale(pygame.image.load("D:\my games\stickman\start_images\Background.png"),(win_width,win_height))
background_level1=pygame.transform.scale(pygame.image.load("D:\my games\stickman\level_1_images\Background.jpg"),(mid_width,mid_height))
background_level2=pygame.transform.scale(pygame.image.load("D:\my games\stickman\level_2_images\Background.png"),(mid_width,mid_height))
background_level3=pygame.transform.scale(pygame.image.load("D:\my games\stickman\level_3_images\Background.png"),(mid_width,mid_height))
background_level4=pygame.transform.scale(pygame.image.load("D:\my games\stickman\level_4_images\Background.png"),(mid_width,mid_height))
background_level5=pygame.transform.scale(pygame.image.load("D:\my games\stickman\level_5_images\Background.png"),(mid_width,mid_height))
background_level6=pygame.transform.scale(pygame.image.load("D:\my games\stickman\level_6_images\Background.png"),(mid_width,mid_height))
background_level7=pygame.transform.scale(pygame.image.load("D:\my games\stickman\level_7_images\Background.png"),(mid_width,mid_height))

start=pygame.transform.scale(pygame.image.load("D:\my games\stickman\start_images\start.png"),(start_width,start_height))
brick=pygame.transform.scale(pygame.image.load("D:\my games\stickman\level_3_images\Brick.png"),(brick_width,brick_height))
back=pygame.transform.scale(pygame.image.load("D:\my games\stickman\default_images\Back.png"),(back_width,back_height))

back_hover=pygame.transform.scale(pygame.image.load("D:\my games\stickman\default_images\Back.png"),(back_width+10,back_height+10))
start_hover=pygame.transform.scale(pygame.image.load("D:\my games\stickman\start_images\start.png"),(start_width+10,start_height+10))


start_rect=pygame.Rect(750,450,start_width,start_height)
back_rect=pygame.Rect(10,25,back_width,back_height)

start_rect_hover=pygame.Rect(745,445,start_width+10,start_height+10)
back_rect_hover=pygame.Rect(8,23,back_width+10,back_height+10)

def window(level):
    win.blit(background,(0,0))
    win.blit(back,(back_rect.x,back_rect.y))

    pos = pygame.mouse.get_pos()
    if back_rect.collidepoint(pos):
        win.blit(back_hover, (back_rect_hover.x, back_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
            levels.main()

    win.blit(start,(start_rect.x,start_rect.y))
    level_name = name.render(level, 1, black)
    win.blit(level_name,(180,25))

    if level=="level1":
        win.blit(background_level1,(0,98))
    elif level=="level2":
        win.blit(background_level2,(0,98))
    elif level=="level3":
        win.blit(background_level3,(0,98))
        win.blit(brick,(450,250))
    elif level=="level4":
        win.blit(background_level4,(0,98))
    elif level=="level5":
        win.blit(background_level5,(0,98))
    elif level=="level6":
        win.blit(background_level6,(0,98))
    elif level=="level7":
        win.blit(background_level7,(0,98))

    pos = pygame.mouse.get_pos()
    if start_rect.collidepoint(pos):
        win.blit(start_hover, (start_rect_hover.x, start_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
            if level=="level1":
                level1.main()
            elif level=="level2":
                level2.main()
            elif level=="level3":
                level3.main()
            elif level=="level4":
                level4.main()
            elif level == "level5":
                level5.main()
            elif level == "level6":
                level6.main()
            elif level == "level7":
                level7.main()

    pygame.display.update()

def main(level):
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        window(level)
    pygame.quit()

if __name__=="__main__":
    main()