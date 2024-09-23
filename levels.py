import pygame
import play
import start


pygame.font.init()

name = pygame.font.SysFont('comicsans', 20)

win_width=1200
win_height=600

black=(0,0,0)
white=(255,255,255)
white=(255,255,255)

home_width=50
home_height=50

star_width=30
star_height=30

home=pygame.transform.scale(pygame.image.load(r"default_images\home.png"),(home_width,home_height))
one=pygame.transform.scale(pygame.image.load(r"default_images\one.png"),(home_width,home_height))
two=pygame.transform.scale(pygame.image.load(r"default_images\Two.png"),(home_width,home_height))
three=pygame.transform.scale(pygame.image.load(r"default_images\Three.png"),(home_width,home_height))
four=pygame.transform.scale(pygame.image.load(r"default_images\Four.jpg"),(home_width,home_height))
five=pygame.transform.scale(pygame.image.load(r"default_images\Five.png"),(home_width,home_height))
six=pygame.transform.scale(pygame.image.load(r"default_images\six.jpg"),(home_width,home_height))
seven=pygame.transform.scale(pygame.image.load(r"default_images\seven.png"),(home_width,home_height))

star=pygame.transform.scale(pygame.image.load(r"default_images\star.png"),(star_width,star_height))

home_hover=pygame.transform.scale(pygame.image.load(r"default_images\home.png"),(home_width+10,home_height+10))
one_hover=pygame.transform.scale(pygame.image.load(r"default_images\one.png"),(home_width+10,home_height+10))
two_hover=pygame.transform.scale(pygame.image.load(r"default_images\Two.png"),(home_width+10,home_height+10))
three_hover=pygame.transform.scale(pygame.image.load(r"default_images\Three.png"),(home_width+10,home_height+10))
four_hover=pygame.transform.scale(pygame.image.load(r"default_images\Four.jpg"),(home_width+10,home_height+10))
five_hover=pygame.transform.scale(pygame.image.load(r"default_images\Five.png"),(home_width+10,home_height+10))
six_hover=pygame.transform.scale(pygame.image.load(r"default_images\six.jpg"),(home_width+10,home_height+10))
seven_hover=pygame.transform.scale(pygame.image.load(r"default_images\seven.png"),(home_width+10,home_height+10))

home_rect=pygame.Rect(10,50,home_width,home_height)
one_rect=pygame.Rect(200,150,home_width,home_height)
two_rect=pygame.Rect(400,150,home_width,home_height)
three_rect=pygame.Rect(600,150,home_width,home_height)
four_rect=pygame.Rect(800,150,home_width,home_height)
five_rect=pygame.Rect(1000,150,home_width,home_height)
six_rect=pygame.Rect(200,300,home_width,home_height)
seven_rect=pygame.Rect(400,300,home_width,home_height)

home_rect_hover=pygame.Rect(8,48,home_width+10,home_height+10)
one_rect_hover=pygame.Rect(198,148,home_width+10,home_height+10)
two_rect_hover=pygame.Rect(398,148,home_width+10,home_height+10)
three_rect_hover=pygame.Rect(598,148,home_width+10,home_height+10)
four_rect_hover=pygame.Rect(798,148,home_width+10,home_height+10)
five_rect_hover=pygame.Rect(998,148,home_width+10,home_height+10)
six_rect_hover=pygame.Rect(198,298,home_width+10,home_height+10)
seven_rect_hover=pygame.Rect(398,298,home_width+10,home_height+10)

def window():
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Stickman Skate")

    win.fill(white)
    level = name.render("Stickman Skate", 1, black)

    win.blit(level,(550,50))

    win.blit(home,(home_rect.x,home_rect.y))
    win.blit(one, (one_rect.x, one_rect.y))
    win.blit(two, (two_rect.x, two_rect.y))
    win.blit(three, (three_rect.x, three_rect.y))
    win.blit(four, (four_rect.x, four_rect.y))
    win.blit(five, (five_rect.x, five_rect.y))
    win.blit(six, (six_rect.x, six_rect.y))
    win.blit(seven,(seven_rect.x,seven_rect.y))

    try:
        f = open(r"level_star\level1_star.txt", "r")
        star_count=f.readline()
        if star_count=="one":
            win.blit(star,(210,110))
        elif star_count=="two":
            win.blit(star,(190,110))
            win.blit(star,(230,110))
        elif star_count=="three":
            win.blit(star,(170,110))
            win.blit(star,(210,110))
            win.blit(star,(250,110))

        f = open(r"level_star\level2_star.txt", "r")
        star_count = f.readline()
        if star_count == "one":
            win.blit(star, (410, 110))
        elif star_count == "two":
            win.blit(star, (390, 110))
            win.blit(star, (430, 110))
        elif star_count == "three":
            win.blit(star, (370, 110))
            win.blit(star, (410, 110))
            win.blit(star, (450, 110))

        f = open(r"level_star\level3_star.txt", "r")
        star_count = f.readline()
        if star_count == "one":
            win.blit(star, (610, 110))
        elif star_count == "two":
            win.blit(star, (590, 110))
            win.blit(star, (630, 110))
        elif star_count == "three":
            win.blit(star, (570, 110))
            win.blit(star, (610, 110))
            win.blit(star, (650, 110))

        f = open(r"level_star\level4_star.txt", "r")
        star_count = f.readline()
        if star_count == "one":
            win.blit(star, (810, 110))
        elif star_count == "two":
            win.blit(star, (790, 110))
            win.blit(star, (830, 110))
        elif star_count == "three":
            win.blit(star, (770, 110))
            win.blit(star, (810, 110))
            win.blit(star, (850, 110))

        f = open(r"level_star\level5_star.txt", "r")
        star_count = f.readline()
        if star_count == "one":
            win.blit(star, (1010, 110))
        elif star_count == "two":
            win.blit(star, (990, 110))
            win.blit(star, (1030, 110))
        elif star_count == "three":
            win.blit(star, (970, 110))
            win.blit(star, (1010, 110))
            win.blit(star, (1050, 110))

        f = open(r"level_star\level6_star.txt", "r")
        star_count = f.readline()
        if star_count == "one":
            win.blit(star, (210, 260))
        elif star_count == "two":
            win.blit(star, (190, 260))
            win.blit(star, (230, 260))
        elif star_count == "three":
            win.blit(star, (170, 260))
            win.blit(star, (210, 260))
            win.blit(star, (250, 260))

        f = open(r"level_star\level7_star.txt", "r")
        star_count = f.readline()
        if star_count == "one":
            win.blit(star, (410, 260))
        elif star_count == "two":
            win.blit(star, (390, 260))
            win.blit(star, (430, 260))
        elif star_count == "three":
            win.blit(star, (370, 260))
            win.blit(star, (410, 260))
            win.blit(star, (450, 260))

    except FileNotFoundError as fnf:
        pass

    pos = pygame.mouse.get_pos()

    if home_rect.collidepoint(pos):
        win.blit(home_hover, (home_rect_hover.x, home_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
            play.main()

    elif one_rect.collidepoint(pos):
        win.blit(one_hover, (one_rect_hover.x, one_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
            start.main("level1")

    elif two_rect.collidepoint(pos):
        win.blit(two_hover, (two_rect_hover.x, two_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
            start.main("level2")


    elif three_rect.collidepoint(pos):
        win.blit(three_hover, (three_rect_hover.x, three_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
            start.main("level3")


    elif four_rect.collidepoint(pos):
        win.blit(four_hover, (four_rect_hover.x, four_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
            start.main("level4")

    elif five_rect.collidepoint(pos):
        win.blit(five_hover, (five_rect_hover.x, five_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
            start.main("level5")

    elif six_rect.collidepoint(pos):
        win.blit(six_hover, (six_rect_hover.x, six_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
            start.main("level6")

    elif seven_rect.collidepoint(pos):
        win.blit(seven_hover, (seven_rect_hover.x, seven_rect_hover.y))
        if pygame.mouse.get_pressed()[0]:
            start.main("level7")

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