import pygame
import random
from Arduino_Monitor import SerialData



#arduino_analog_input
ard_an = SerialData()


#Define color
BLACK=(  0,   0,   0)
WHITE=(255, 255, 255)
GREEN=(  0, 255,  0 )
RED=(255,   0,  0 )
BLUE=(  0,   0, 255)




pygame.init()
screen_x = 800
screen_y = 550
pad_x = 400
click_sound = pygame.mixer.Sound("/usr/share/kde4/apps/marble/data/audio/KDE-Sys-List-End.ogg")
#background_image = pygame.image.load("pic.jpg").convert()


size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("MEDLAID_cool_game")

done = False


clock = pygame.time.Clock()
circle_posx = 100
circle_posy = 100
circle_speedx = 5
circle_speedy = 5



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # ______game logic__________
     
    #pos = int(ard_an.next()/1.6)
    #mouse_pos = pygame.mouse.get_pos()
    #bar_x = mouse_pos[0]
    bar_x = int(ard_an.next()/1.28)
    circle_posx += circle_speedx #* random.randrange(1,10)
    circle_posy += circle_speedy #* random.randrange(1,5)
    if circle_posx > screen_x - 30:
        circle_speedx = -(random.randint(5,20))
    if circle_posx < 30:
        circle_speedx = random.randint(5,20)

    if circle_posy > screen_y - 30 and circle_posx > bar_x and circle_posx < bar_x + 100:
        circle_speedy = -5
        click_sound.play()
    #if circle_posy > screen_y:
     #   done = True



    if circle_posy < 30:
        circle_speedy = 5
        click_sound.play()
    if bar_x > 680:
        bar_x = 680
        click_sound.play()
    if bar_x < 20:
        bar_x = 20
        click_sound.play()












    # ________drawing code ______
    screen.fill(WHITE)
    pygame.draw.circle(screen,BLACK,(circle_posx,circle_posy),10)
    pygame.draw.rect(screen,RED,((0,0),(20,screen_y)))
    pygame.draw.rect(screen,RED,((20,0),(screen_x-20,20)))
    pygame.draw.rect(screen,RED,((780,0),(20,screen_y)))
    pygame.draw.rect(screen,BLUE,((bar_x,530),(100,20)))
    #pygame.draw.line(screen,GREEN,(100,200),(300,400),20)
    
    
    #screen.blit(background_image, [0, 0])







    pygame.display.flip()


    clock.tick(60)


pygame.quit()

