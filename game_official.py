import pygame
import time
import random


pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 255, 0)

bright_red=(255,0,0)

bright_green=(255,0,0)

grey_color = (170, 170, 170)

dark_grey_color = (85,85,85)

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('I Will be a Hackkkerrrr')


clock = pygame.time.Clock()

it_nerdImg = pygame.image.load('it-nerd[resize].png')

icon = pygame.image.load("icon.png")
icon = pygame.transform.scale(icon, (128,128))

pygame.display.set_icon(icon)

level_1_scene = pygame.image.load('scene_.png')

pcImg = pygame.image.load('pc.png')
pcImg = pygame.transform.scale(pcImg,(64,64))

hackcook_bookImg = pygame.image.load('hackcook_book.png')
hackcook_bookImg = pygame.transform.scale(hackcook_bookImg,(64,64))

hoodieImg = pygame.image.load('hoodie.png')
hoodieImg = pygame.transform.scale(hoodieImg, (64,64))

popSound = pygame.mixer.Sound('it-nerd.wav')

#level_1_scene = pygame.transform.scale(level_1_scene, (display_width, display_height))


it_nerd_width = 45

def find_computer(recx, recy, recw, rech, color):
    pygame.draw.rect(gameDisplay, dark_grey_color, [recx, recy, recw, rech])

def find_hackcookbook(hackx, hacky, hackw, hackh, color):
    pygame.draw.rect(gameDisplay, grey_color, [hackx, hacky, hackw, hackh])

def find_hoodie(hoodiex, hoodiey, hoodiew, hoodieh, color):
    pygame.draw.rect(gameDisplay, [255, 255, 255], [hoodiex,hoodiey,hoodiew,hoodieh], 1)
    #pygame.draw.rect(gameDisplay, bright_red, [hoodiex, hoodiey, hoodiew, hoodieh])

def it_nerd(x, y):
    gameDisplay.blit(it_nerdImg, (x, y))

def pc(x,y):
    gameDisplay.blit(pcImg, (x,y))

def hack_cookbook(x,y):
    gameDisplay.blit(hackcook_bookImg, (x,y))

def hoodie(x,y):
    gameDisplay.blit(hoodieImg, (x,y))

def scene(lvlx,lvly):
    gameDisplay.blit(level_1_scene, (lvlx, lvly))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 55)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2)), ((display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()



def button(msg, x, y, w, h,ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def pygame_quit():
    pygame.quit()
    quit()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 75)
        TextSurf, TextRect = text_objects("I will be a hackerr", largeText)
        TextRect.center = ((display_width/2)), ((display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Go!", 150, 450, 100, 50, green, bright_green, game_loop)
        pygame.mixer.Sound.play(popSound)
        button("Quit", 550, 450, 100, 50, red, bright_red, pygame_quit)

        # pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))

        pygame.display.update()
        clock.tick(15)

level = 0

def crash(level):
    message_display('You found it!')
    level = level + 1
    return level

def game_scene():
    gameDisplay.fill(white)

def game_loop():
    #x = (display_width * 0.45)
    #y = (display_height * 0.8)

    x = 150
    y = 150



    x_change = 0
    y_change = 0

    recx = 700
    recy = 572
    recw = 25
    rech = 25

    hackx = 530
    hacky = 65
    hackw = 25
    hackh = 25

    hoodiex = 280
    hoodiey = 400
    hoodiew = 45
    hoodieh = 50

    pcFound = False
    hack_cookbookFound = False
    hoodieFound = False

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change

        y += y_change


        scene(0,0)


        find_computer(recx, recy, recw, rech, bright_red)
        find_hackcookbook(hackx, hacky, hackw, hackh, bright_red)
        find_hoodie(hoodiex, hoodiey, hoodiew, hoodieh, bright_red)

        it_nerd(x,y)


        if y < recy + rech and y > recy - rech:


            if  x > recx and x < recx + recw or x + it_nerd_width > recx and x + it_nerd_width < recx + recw:
                pcFound = True
                print(pcFound)
                #Found PC

        if y < hacky + hackh and y > hacky - hackh:


            if x > hackx and x < hackx + hacky or x + it_nerd_width > hackx and x + it_nerd_width < hackx + hackw:
                hack_cookbookFound = True
                print (hack_cookbookFound)



        if y < hoodiey + hoodieh and y > hoodiey - hoodieh:


            if x > hoodiex and x > hoodiex + hoodiey or x + it_nerd_width > hoodiex and x - it_nerd_width < hoodiex + hoodiew:
                hoodieFound = True
                print (hoodieFound)

                # Found Black Hoodie

        if pcFound == True:
            pc(150, 35)

        if hack_cookbookFound == True:
            hack_cookbook(50,35)

        if hoodieFound == True:
            hoodie(250, 35)

        if pcFound and hack_cookbookFound and hoodieFound == True:
            pygame.mixer.Sound.play(popSound)
            message_display('You a expert haker')


        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()


