import pygame
import levels
import os

pygame.font.init()
pygame.mixer.init()

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

    level=font.render("Level 6",1,black)
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

win_width = 1200
win_height = 600

stickman_width = 50
stickman_height = 100

stickman_vel = 4

stickman_jump_height=100

background = pygame.image.load(os.path.join(r"level_6_images\Background.png"))
winflag = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\winflag.png")),(75, 150))

stickman_stand = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\stickman_stand.png")),(stickman_width, stickman_height))
stickman_skate = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\stickman_skate.png")),(stickman_width, stickman_height))

stickman_left_stand = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\stickman_left_stand.png")),(stickman_width, stickman_height))
stickman_left_skate = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\stickman_left_skate.png")),(stickman_width, stickman_height))

pause = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\pause.png")),(play_width, play_height))
pause_hover = pygame.transform.scale(pygame.image.load(os.path.join(r"default_images\pause.png")),(play_width + 10, play_height + 10))

stickman_rect = pygame.Rect(50, 400, stickman_width, stickman_height)
pause_rect = pygame.Rect(15, 20, play_width, play_height)
pipe1_rect=pygame.Rect(1020,420,180,180)
pipe2_rect=pygame.Rect(1020,120,180,180)

pause_rect_hover = pygame.Rect(13, 18, play_width + 10, play_height + 10)

def window(pressed,count,rects):
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Stickman-----LEVEL-6")

    win.blit(background,(0,0))

    if count<90:
        level=level_font.render("LEVEL 6",1,black)
        sugg=font.render("Press UP arrow to travel through pipes",1,black)
        win.blit(level,(300,25))
        win.blit(sugg,(300,100))
        win.blit(font.render("Press DOWN arrow to travel through pipes",1,black),(300,125))
    count+=1

    win.blit(winflag,(100,50))
    win.blit(pause, (pause_rect.x, pause_rect.y))

    pos = pygame.mouse.get_pos()

    key_pressed = pygame.key.get_pressed()

    #   right move

    if key_pressed[pygame.K_RIGHT] and stickman_rect.x+stickman_width < 1200 and stickman_rect.x > 0:
        pressed = 0
        if key_pressed[pygame.K_SPACE] and stickman_rect.x<1020:
            stickman_rect.y-=stickman_jump_height
            stickman_rect.x+=stickman_vel
            win.blit(stickman_skate,(stickman_rect.x,stickman_rect.y))
            if stickman_rect.x>1020 and (stickman_rect.y==300 or stickman_rect.y==0):
                pass
            else:
                stickman_rect.y += stickman_jump_height
        elif stickman_rect.y>=300 and key_pressed[pygame.K_UP]:
            stickman_rect.y=0
        elif stickman_rect.y>=0 and stickman_rect.y<100 and key_pressed[pygame.K_DOWN]:
            stickman_rect.y=300
        else:
            if stickman_rect.colliderect(pipe1_rect) or stickman_rect.colliderect(pipe2_rect):
                win.blit(stickman_stand,(stickman_rect.x,stickman_rect.y))
                stickman_rect.x-=stickman_vel
            else:
                stickman_rect.x += stickman_vel
                win.blit(stickman_skate, (stickman_rect.x, stickman_rect.y))

    #   left move

    elif key_pressed[pygame.K_LEFT] and stickman_rect.x< 1200 and stickman_rect.x > 0:
        pressed=1
        if key_pressed[pygame.K_SPACE] and stickman_rect.x<1020:
            stickman_rect.y-=stickman_jump_height
            stickman_rect.x-=stickman_vel
            win.blit(stickman_left_skate,(stickman_rect.x,stickman_rect.y))
            if stickman_rect.x>1020 and (stickman_rect.y==300 or stickman_rect.y==0):
                pass
            else:
                stickman_rect.y += stickman_jump_height
        elif stickman_rect.y>=300 and key_pressed[pygame.K_UP]:
            stickman_rect.y=0
        elif stickman_rect.y>=0 and stickman_rect.y<100 and key_pressed[pygame.K_DOWN]:
            stickman_rect.y=300
        elif stickman_rect.x+stickman_width<1020 and (stickman_rect.y==300 or stickman_rect.y==0):
            stickman_rect.y+=stickman_jump_height
        else:
            stickman_rect.x -= stickman_vel
            win.blit(stickman_left_skate, (stickman_rect.x, stickman_rect.y))

    #   right and left jump

    elif key_pressed[pygame.K_SPACE] and stickman_rect.x<1200 and stickman_rect.x>0 :
        if pressed==0:
            if stickman_rect.x > 1020:
                win.blit(stickman_stand, (stickman_rect.x, stickman_rect.y))
            else:
                stickman_rect.y -= stickman_jump_height
                win.blit(stickman_stand, (stickman_rect.x, stickman_rect.y))
                stickman_rect.y += stickman_jump_height
        elif pressed==1:
            if stickman_rect.x > 1020:
                win.blit(stickman_left_stand, (stickman_rect.x, stickman_rect.y))
            else:
                stickman_rect.y -= stickman_jump_height
                win.blit(stickman_left_stand, (stickman_rect.x, stickman_rect.y))
                stickman_rect.y += stickman_jump_height

    elif key_pressed[pygame.K_ESCAPE]:
        runs=pause_main()
        if runs=="start again":
            stickman_rect.x=50
            stickman_rect.y=332

    elif pause_rect.collidepoint(pos):
        win.blit(pause_hover, (pause_rect_hover.x, pause_rect_hover.y))
        if pressed == 0:
            win.blit(stickman_stand, (stickman_rect.x, stickman_rect.y))
        elif pressed == 1:
            win.blit(stickman_left_stand, (stickman_rect.x, stickman_rect.y))
        if pygame.mouse.get_pressed()[0]:
            runs=pause_main()
            if runs == "start again":
                stickman_rect.x = 50
                stickman_rect.y = 370

    #   Standing Code

    else:
        if stickman_rect.x > 1020 :
            if stickman_rect.y >= 300 and key_pressed[pygame.K_UP]:
                stickman_rect.y = 0
            elif stickman_rect.y >= 0 and stickman_rect.y < 100 and key_pressed[pygame.K_DOWN]:
                stickman_rect.y = 300
        if pressed == 0:
            win.blit(stickman_stand, (stickman_rect.x, stickman_rect.y))
        elif pressed == 1:
            win.blit(stickman_left_stand, (stickman_rect.x, stickman_rect.y))

    pygame.display.update()

    if stickman_rect.x <50 and stickman_rect.y<=170:
        f = open(r"level_star\level6_star.txt", "w")
        f.write("three")
        levels.main()

    return pressed,count,rects

def main():

    clock=pygame.time.Clock()
    run=True
    count=0
    pressed=0
    rects=0
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        pressed,count,rects=window(pressed,count,rects)
    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    main()