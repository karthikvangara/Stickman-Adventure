import pygame
import levels
import os


play_width = 50
play_height = 50

white=(255,255,255)
black=(0,0,0)

font = pygame.font.SysFont('comicsans', 20)
level_font = pygame.font.SysFont('comicsans', 50)


# pause code

play_img = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\play.png")),(play_width, play_height))
play_img_hover = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\play.png")),(play_width + 10, play_height + 10))

restart = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\Restart.png")),(play_width, play_height))
restart_hover = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\Restart.png")),(play_width + 10, play_height + 10))

quit_img = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\quit.jpg")),(play_width, play_height))
quit_img_hover = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\quit.jpg")),(play_width + 10, play_height + 10))

play_img_rect = pygame.Rect(100, 220, play_width, play_height)
restart_rect = pygame.Rect(220, 220, play_width, play_height)
quit_img_rect = pygame.Rect(340, 220, play_width, play_height)

play_img_rect_hover = pygame.Rect(98, 218, play_width + 10, play_height + 10)
restart_rect_hover = pygame.Rect(218, 218, play_width + 10, play_height + 10)
quit_rect_img_hover = pygame.Rect(338, 218, play_width + 10, play_height + 10)


def pause_window(runs):

    pause_win_width=500
    pause_win_height=300

    pause_win=pygame.display.set_mode((pause_win_width,pause_win_height))
    pygame.display.set_caption("Paused")

    pause_win.fill(white)

    level=font.render("Level 4",1,black)
    pause_win.blit(level,(200,100))

    pause_win.blit(play_img,(play_img_rect.x,play_img_rect.y))
    pause_win.blit(restart, (restart_rect.x, restart_rect.y))
    pause_win.blit(quit_img, (quit_img_rect.x, quit_img_rect.y))

    pos=pygame.mouse.get_pos()

    if play_img_rect.collidepoint(pos):
        pause_win.blit(play_img_hover,(play_img_rect_hover.x,play_img_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
            main()

    elif restart_rect.collidepoint(pos):
        pause_win.blit(restart_hover,(restart_rect_hover.x,restart_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
            runs=False

    elif quit_img_rect.collidepoint(pos):
        pause_win.blit(quit_img_hover, (quit_rect_img_hover.x, quit_rect_img_hover.y))
        if pygame.mouse.get_pressed()[0]:
            levels.main()

    pygame.display.update()

    return runs

def pause_main():
    run=True
    runs=True
    while run and runs:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        runs=pause_window(runs)
    if runs==False:
        return "start again"
    else:
        return



#   level code


win_width=1200
win_height=600

stickman_width=50
stickman_height=100

stickman_jump_height=100

brick_width=212
brick_height=35

stickman_vel=4

black=(0,0,0)

level_font = pygame.font.SysFont('comicsans', 50)

background=pygame.image.load(os.path.join(r"level_4_images\Background.png"))
winflag=pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\winflag.png")),(75,150))

stickman_stand=pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\stickman_stand.png")),(stickman_width,stickman_height))
stickman_skate=pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\stickman_skate.png")),(stickman_width,stickman_height))

stickman_left_stand=pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\stickman_left_stand.png")),(stickman_width,stickman_height))
stickman_left_skate=pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\stickman_left_skate.png")),(stickman_width,stickman_height))

pause = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\pause.png")),(play_width, play_height))
pause_hover = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\pause.png")),(play_width + 10, play_height + 10))

stickman_rect=pygame.Rect(100,360,stickman_width,stickman_height)
pause_rect = pygame.Rect(15, 20, play_width, play_height)
jump_rect=pygame.Rect(490,360,710,340)

pause_rect_hover = pygame.Rect(13, 18, play_width + 10, play_height + 10)

def window(pressed,count,count_jump,count_jump_left):
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Stickman-----LEVEL-4")

    win.blit(background,(0,0))

    if count<90:
        level=level_font.render("LEVEL 4",1,black)
        win.blit(level,(300,200))
    count+=1

    win.blit(winflag,(950,215))

    win.blit(pause,(pause_rect.x,pause_rect.y))

    pos = pygame.mouse.get_pos()

    key_pressed = pygame.key.get_pressed()

    #   right move

    if key_pressed[pygame.K_RIGHT] and stickman_rect.x < 950:
        pressed=0
        space_pressed=pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE] and not jump_rect.colliderect(stickman_rect):
            stickman_rect.y-=stickman_jump_height
            stickman_rect.x+=stickman_vel
            win.blit(stickman_skate,(stickman_rect.x,stickman_rect.y))
            stickman_rect.y+=stickman_jump_height

        elif jump_rect.colliderect(stickman_rect) and key_pressed[pygame.K_SPACE]:
            stickman_rect.y-=stickman_jump_height
            stickman_rect.x+=10

        elif jump_rect.colliderect(stickman_rect):
            win.blit(stickman_skate,(stickman_rect.x,stickman_rect.y))

        else:
            stickman_rect.x+=stickman_vel
            win.blit(stickman_skate,(stickman_rect.x,stickman_rect.y))

    #   left move

    elif key_pressed[pygame.K_LEFT] and stickman_rect.x < 950 and stickman_rect.x > 0:
        pressed=1
        space_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE] and (stickman_rect.x!=405 and stickman_rect.x!=408):
            stickman_rect.y -= stickman_jump_height
            stickman_rect.x -= stickman_vel
            win.blit(stickman_left_skate, (stickman_rect.x, stickman_rect.y))
            stickman_rect.y += stickman_jump_height

        elif stickman_rect.x+stickman_width<490 and stickman_rect.y==260:
            stickman_rect.y+=stickman_jump_height

        else:
            stickman_rect.x -= stickman_vel
            win.blit(stickman_left_skate, (stickman_rect.x, stickman_rect.y))




    #   right and left jump

    elif key_pressed[pygame.K_SPACE] and stickman_rect.x<950 :
        if pressed==0:
            stickman_rect.y -= stickman_jump_height
            win.blit(stickman_stand, (stickman_rect.x, stickman_rect.y))
            stickman_rect.y += stickman_jump_height
        elif pressed==1:
            stickman_rect.y -= stickman_jump_height
            win.blit(stickman_left_stand, (stickman_rect.x, stickman_rect.y))
            stickman_rect.y += stickman_jump_height

    elif key_pressed[pygame.K_ESCAPE]:
        runs=pause_main()
        if runs=="start again":
            stickman_rect.x=100
            stickman_rect.y=360

    elif pause_rect.collidepoint(pos):
        win.blit(pause_hover, (pause_rect_hover.x, pause_rect_hover.y))
        if pressed == 0:
            win.blit(stickman_stand, (stickman_rect.x, stickman_rect.y))
        elif pressed == 1:
            win.blit(stickman_left_stand, (stickman_rect.x, stickman_rect.y))
        if pygame.mouse.get_pressed()[0]:
            runs=pause_main()
            if runs == "start again":
                stickman_rect.x = 100
                stickman_rect.y = 360


    else:
        if pressed == 0:
            win.blit(stickman_stand, (stickman_rect.x, stickman_rect.y))
        elif pressed == 1:
            win.blit(stickman_left_stand, (stickman_rect.x, stickman_rect.y))

    pygame.display.update()

    if stickman_rect.x >= 950 and stickman_rect.y<=342:
        f = open(r"level_star\level4_star.txt", "w")
        f.write("three")
        levels.main()

    return pressed,count,count_jump,count_jump_left

def main():

    clock=pygame.time.Clock()
    run=True
    count=0
    pressed=0
    count_jump=0
    count_jump_left=0
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        pressed,count,count_jump,count_jump_left=window(pressed,count,count_jump,count_jump_left)
        if pressed==-1:
            run=False
    pygame.quit()

if __name__=="__main__":
    pygame.init()
    main()